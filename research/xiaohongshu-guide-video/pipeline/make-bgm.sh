#!/usr/bin/env bash
# Generate the calm lo-fi background bed used by the guide video (warm, low, unobtrusive).
set -e
FF="$(node -e 'process.stdout.write(require("ffmpeg-static"))')"
"$FF" -y \
 -f lavfi -i "sine=frequency=261.63:duration=158" \
 -f lavfi -i "sine=frequency=329.63:duration=158" \
 -f lavfi -i "sine=frequency=392.00:duration=158" \
 -f lavfi -i "aevalsrc=0.6*sin(2*PI*523.25*t)*exp(-6*mod(t\,0.75)):d=158" \
 -f lavfi -i "aevalsrc=0.5*sin(2*PI*659.25*t)*exp(-6*mod(t+0.375\,0.75)):d=158" \
 -filter_complex "[0:a]volume=0.16[p0];[1:a]volume=0.12[p1];[2:a]volume=0.10[p2];\
  [p0][p1][p2]amix=inputs=3:normalize=0,tremolo=f=0.18:d=0.25,lowpass=f=1400[pad];\
  [3:a]volume=0.10,lowpass=f=2600[pl1];[4:a]volume=0.08,lowpass=f=2600[pl2];\
  [pad][pl1][pl2]amix=inputs=3:normalize=0,afade=t=in:st=0:d=3,afade=t=out:st=153:d=4,\
   loudnorm=I=-21:TP=-2:LRA=11,alimiter=limit=0.85[mix]" \
 -map "[mix]" -ar 44100 -t 158 -c:a pcm_s16le .bgm.wav
echo "wrote .bgm.wav"
