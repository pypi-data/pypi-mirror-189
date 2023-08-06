#!/usr/bin/env bash

set -euxo pipefail

sink_device="alsa_output.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.analog-stereo"
sink_device_id=$(pactl list sinks short | grep "$sink_device" | cut -f 1)
source_device="alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.mono-fallback"
source_device_id=$(pactl list sources short | grep "$source_device" | cut -f 1)

wine_client=$(pactl list clients short | grep wine-preloader | cut -f 1)
wine_sink_input=$(pactl list sink-inputs short | grep -E "[0-9]\s+[0-9]\s+${wine_client}" | cut -f 1)
wine_source_output=$(pactl list source-outputs short | grep -E "[0-9]\s+[0-9]\s+${wine_client}" | cut -f 1)

pactl move-sink-input $wine_sink_input $sink_device_id
pactl move-source-output $wine_source_output $source_device_id
