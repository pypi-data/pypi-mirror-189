#  Copyright 2023 Synnax Labs, Inc.
#
#  Use of this software is governed by the Business Source License included in the file
#  licenses/BSL.txt.
#
#  As of the Change Date specified in that file, in accordance with the Business Source
#  License, use of this software will be governed by the Apache License, Version 2.0,
#  included in the file licenses/APL.txt.

import fnmatch

from synnax import Channel
from synnax.cli.flow import Context
from synnax.cli.select import select_from_table


def channel_name_table(
    ctx: Context,
    names: list[str],
):
    ctx.console.table(
        columns=["name"],
        rows=[{"name": name} for i, name in enumerate(names)],
    )


def maybe_select_channel(
    ctx: Context,
    channels: list[Channel],
    param: str,
) -> Channel | None:
    """Asks the user to select a channel if there are multiple channels available.

    :param ctx: The current flow context.
    :param channes:  The list of channels to prompt frome.
    :returns: The selected channel or None if there are no channels.
    """
    if len(channels) == 0:
        return None
    if len(channels) > 1:
        ctx.console.error(f"Multiple channels found for {param}!")
        selected = select_channel(ctx, channels, allow_none=True)
        if not selected:
            return None
    return channels[0]


def select_channel(
    ctx: Context,
    channels: list[Channel],
    default: str | None = None,
    allow_none: bool = False,
) -> Channel | None:
    """Prompts the user to select a channel from a list of channels.

    :param ctx: The current flow Context.
    :param channels: The list of channels to select from.
    :param default: The default channel to select.
    :param allow_none: Whether to allow the user to select None.
    """

    try:
        _default = [c.key for c in channels].index(default) if default else None
    except ValueError as e:
        raise ValueError(f"Invalid default channel: {default}") from e

    i = select_from_table(
        ctx,
        columns=["name", "key", "data_type", "index", "rate", "node_id"],
        rows=[{k: f"{v}" for k, v in c.dict().items()} for c in channels],
        required=allow_none,
        default=_default,
    )
    return channels[i] if i is not None else None


def prompt_group_channel_names(
    ctx: Context, options: list[str]
) -> dict[str, list[str]] | None:
    """Prompts the user to group channel names by providing a list of matchers.

    :param ctx: The current flow Context.
    :param options: The list of channel names to match against.
    """
    ctx.console.info(
        """You can enter 'all' for all channels or a comma-separated list of:
    1) Names (e.g. 'channel1, channel2, channel3')
    2) Channel indices (e.g. '1, 2, 3')
    3) A pattern to match (e.g. 'channel*, sensor*')
    """
    )
    res = ctx.console.ask("Channels")
    if res is None:
        if ctx.console.confirm(
            "No valid pattern provided. Would you like to try again?"
        ):
            return prompt_group_channel_names(ctx, options)
        return None

    return group_channel_names(ctx, options, res.split(","))


def group_channel_names(
    ctx: Context,
    options: list[str],
    matchers: list[str],
):
    """Groups channel names by matching them against a list of matchers.

    :param ctx: The current flow Context.
    :param options: The list of channel names to match against.
    :param matchers: The list of matchers to use. Each matcher can be:
    - A name of a channel (e.g. 'channel1')
    - An index of a channel (e.g. '1')
    - A pattern to match (e.g. 'channel*')
    """
    print(matchers, "Time" in options)
    grouped = {}
    for entry in matchers:
        entry = entry.strip()
        channels = []
        if entry.isdigit():
            index = int(entry)
            if index < 0 or index >= len(options):
                ctx.console.error(f"Invalid channel index: {index}[/]")
                if not ctx.console.confirm("Skip?"):
                    return None
                continue
            channels.append(options[index])
        else:
            found = False
            for channel in options:
                if fnmatch.fnmatch(channel, entry) or channel == entry:
                    channels.append(channel)
                    found = True
            if not found:
                ctx.console.error(f"[red]No channels found matching {entry}[/]")
                if not ctx.console.confirm("Skip?"):
                    return None
        grouped[entry] = channels

    return grouped
