#!/bin/bash
# Rebuilds the production environment in a fresh cloud container (containers are ephemeral).
# Everything here is free/open-source and fetched from apt, PyPI or GitHub releases (the hosts this environment allows).
set -e
export DEBIAN_FRONTEND=noninteractive
apt-get update -q
apt-get install -y -q sox libsox-fmt-all fluidsynth rubberband-cli p7zip-full unar \
  dragonfly-reverb-vst3 dpf-plugins-vst3 fluid-soundfont-gm avldrums.lv2-soundfont
pip install -q librosa scipy soundfile pyloudnorm pedalboard matplotlib mido pretty_midi libarchive-c
T=$(mktemp -d)
curl -sL -o $T/surge.deb https://github.com/surge-synthesizer/releases-xt/releases/download/1.3.4/surge-xt-linux-x64-1.3.4.deb
curl -sL -o $T/chow.deb https://github.com/jatinchowdhury18/AnalogTapeModel/releases/download/v2.11.4/ChowTapeModel-Linux-x64-2.11.4.deb
apt-get install -y -q $T/surge.deb $T/chow.deb
curl -sL -o $T/dexed.zip https://github.com/asb2m10/dexed/releases/download/v1.0.1/Dexed-1.0.1-lnx.zip
unzip -o -q $T/dexed.zip -d $T/dexed && cp -r $T/dexed/Dexed.vst3 /usr/lib/vst3/
# sample libraries (shallow git clones; licences recorded in sound_library/asset_manifest.csv)
cd "$(dirname "$0")/../sound_library/incoming"
for r in sfzinstruments/SalamanderGrandPiano sfzinstruments/virtuosity_drums sgossner/VSCO-2-CE \
         sfzinstruments/karoryfer.meatbass sfzinstruments/karoryfer.big-rusty-drums sfzinstruments/karoryfer.growlybass \
         sfzinstruments/SplendidGrandPiano sfzinstruments/karoryfer.black-and-green-guitars sfzinstruments/karoryfer.bear-sax; do
  n=$(basename $r); [ -d $n ] || git clone -q --depth 1 https://github.com/$r $n
done
echo "environment ready"
