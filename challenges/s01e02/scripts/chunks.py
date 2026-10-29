import sys, re, subprocess, json
import numpy as np
from faster_whisper import WhisperModel
from faster_whisper.audio import decode_audio
model = WhisperModel("large-v2", device="cpu", compute_type="int8")
for path in sys.argv[1:]:
    err = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",path,"-af","silencedetect=noise=-35dB:d=0.35","-f","null","-"],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r"silence_start: ([0-9.]+)",err)]
    en=[float(x) for x in re.findall(r"silence_end: ([0-9.]+)",err)]
    audio = decode_audio(path, sampling_rate=16000)
    dur=len(audio)/16000
    # speech spans between silences
    spans=[]; prev=0.0
    for s,e in zip(st,en):
        if s-prev>0.05: spans.append((prev,s))
        prev=e
    if dur-prev>0.05: spans.append((prev,dur))
    name=path.rsplit("/",1)[-1].rsplit(".",1)[0]
    out=[]
    for a,b in spans:
        lo=max(0,a-0.15); hi=min(dur,b+0.15)
        seg=audio[int(lo*16000):int(hi*16000)]
        segs,_=model.transcribe(seg,language="en",beam_size=5,word_timestamps=True,condition_on_previous_text=False,vad_filter=False)
        text=" ".join(s.text.strip() for s in segs)
        out.append({"start":round(a,3),"end":round(b,3),"text":text})
        print(f"{name} [{a:7.3f}-{b:7.3f}] {text}",flush=True)
    json.dump(out,open(f"out/{name}.chunks.json","w"),indent=1)
