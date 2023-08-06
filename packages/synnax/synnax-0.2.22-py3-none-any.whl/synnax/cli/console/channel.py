#  Copyright 2023 Synnax Labs, Inc.
#
#  Use of this software is governed by the Business Source License included in the file
#  licenses/BSL.txt.
#
#  As of the Change Date specified in that file, in accordance with the Business Source
#  License, use of this software will be governed by the Apache License, Version 2.0,
#  included in the file licenses/APL.txt.
#
#  Use of this software is governed by the Business Source License included in the file
#  licenses/BSL.txt.
#
#  As of the Change Date specified in that file, in accordance with the Business Source
#  License, use of this software will be governed by the Apache License, Version 2.0,
#  included in the file licenses/APL.txt.

import fnmatch

from ..flow import Context


def prompt_group_channel_names(
    ctx: Context,
    channels: list[str],
) -> dict[str, list[str]] | None:
    ctx.console.info(
        """
    You can enter 'all' for all channels or a comma-separated list of:
    1) Names (e.g. 'channel1, channel2, channel3')
    2) Channel indices (e.g. '1, 2, 3')
    3) A pattern to match (e.g. 'channel*, sensor*')
    4) A combination of the above (e.g. '1, 2, channel3, my_dog*')
    """
    )
    res = ctx.console.ask("channels", required=True)
    assert res is not None
    return group_channel_names(ctx, channels, res.split(","))


def group_channel_names(
    ctx: Context,
    all_names: list[str],
    matchers: list[str],
):
    grouped = {}
    for entry in matchers:
        entry = entry.strip()
        channels = []
        if entry.isdigit():
            index = int(entry)
            if index < 0 or index >= len(all_names):
                ctx.console.error(f"Invalid channel index: {index}")
                continue
            channels.append(all_names[index])
        else:
            for name in all_names:
                if fnmatch.fnmatch(name, entry):
                    channels.append(name)
            if not channels:
                ctx.console.error(f"No channels match pattern: {entry}")
                if not ctx.console.confirm("Continue?", default=True):
                    return None
        grouped[entry] = channels
    return grouped
