#!/usr/bin/env python
"""Builds the 30-clip sample manifest used by E5 (streaming) and E8 (throughput
and WER control) from the full manifest.

The sample is stratified by source: 20 Huqariq clips and 10 Siminchik clips.
`sample_30_clips.csv` lists them by their path inside the IWSLT 2026 corpus
repository, so no transcription or speaker data is redistributed here.

Usage:
    python build_manifest_from_iwslt.py --corpus-root /path/to/IWSLT2026_Quechua_data --out manifest.csv
    python select_sample.py --manifest manifest.csv --ids sample_30_clips.csv --out manifest_e5_sample.csv
"""
import argparse
import csv


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True, help="full manifest from build_manifest_from_iwslt.py")
    ap.add_argument("--ids", default="sample_30_clips.csv")
    ap.add_argument("--out", default="manifest_e5_sample.csv")
    a = ap.parse_args()

    with open(a.ids, encoding="utf-8") as f:
        wanted = [r["corpus_relpath"] for r in csv.DictReader(f)]
    with open(a.manifest, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)

    by_rel = {}
    for r in rows:
        p = r["audio_path"].replace("\\", "/")
        i = p.find("que_spa_")
        if i >= 0:
            by_rel[p[i:]] = r
    missing = [w for w in wanted if w not in by_rel]
    if missing:
        raise SystemExit(f"{len(missing)} sample clips not found in the manifest, e.g. {missing[0]}")

    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for k in wanted:
            w.writerow(by_rel[k])
    print(f"wrote {len(wanted)} clips to {a.out}")


if __name__ == "__main__":
    main()
