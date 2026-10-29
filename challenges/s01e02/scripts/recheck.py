import sys, json
from faster_whisper import WhisperModel
from faster_whisper.audio import decode_audio
model = WhisperModel("large-v2", device="cpu", compute_type="int8")
prompt = "Nightly batch. Scheduled for three forty-five. Invites moved, two thousand, one hundred and forty. Billed, within limits. Support queue, open."
for path, name, pats in [("media/status-line.mp3","status-line",["for 3","at 3","438","5.19","Build","Cue","Support","Past","past"]),("media/crank-review.mp4","crank-review",["1.","2.","3.","batch 1","Badge"])]:
    audio = decode_audio(path, sampling_rate=16000)
    for c in json.load(open(f"out/{name}.chunks.json")):
        if not any(p in c["text"] for p in pats): continue
        seg = audio[int(max(0,c["start"]-0.15)*16000):int((c["end"]+0.15)*16000)]
        r=[]
        for ip in (None, prompt):
            segs,_ = model.transcribe(seg, language="en", beam_size=5, initial_prompt=ip, condition_on_previous_text=False, temperature=0)
            r.append(" ".join(s.text.strip() for s in segs))
        print(f"{name} {c['start']:7.3f} | {c['text']} | {r[0]} | {r[1]}", flush=True)
