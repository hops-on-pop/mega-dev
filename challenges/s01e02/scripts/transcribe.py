import sys, json
from faster_whisper import WhisperModel
model = WhisperModel("large-v2", device="cpu", compute_type="int8")
for path in sys.argv[1:]:
    segs, info = model.transcribe(path, language="en", word_timestamps=True, beam_size=5, vad_filter=False, condition_on_previous_text=False)
    out = []
    for s in segs:
        out.append({"start": s.start, "end": s.end, "text": s.text,
                    "words": [{"w": w.word, "s": w.start, "e": w.end, "p": w.probability} for w in s.words]})
        print(f"[{s.start:7.2f}-{s.end:7.2f}] {s.text}", flush=True)
    name = path.rsplit("/",1)[-1].rsplit(".",1)[0]
    json.dump(out, open(f"out/{name}.json","w"), indent=1)
