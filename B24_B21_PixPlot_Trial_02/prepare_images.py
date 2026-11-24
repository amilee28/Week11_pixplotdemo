"""Build the combined image set for PixPlot Trial 02 (B24 + B21 photos)."""

import os
import shutil

CLIP = "/Users/leehoiching/.workbuddy-ai/clipboard-images"
SRC_B24 = "/Users/leehoiching/Desktop/week5/B24_photo"
DEST_IMAGES = "/Users/leehoiching/WorkBuddy AI/2026-11-17-16-44-45/B24_PixPlot_Trial_02/images"

# Attachment order (@image#1 .. @image#37) -> filename given by the user.
B21 = [
    ("230Z-459aca56", "B21P35.jpg"),
    ("232Z-76a51bb5", "B21P37.jpg"),
    ("233Z-b2a56f37", "B21P20.jpg"),
    ("234Z-95823aaf", "B21P21.jpg"),
    ("235Z-77b05321", "B21P09.jpg"),
    ("237Z-4304dc1f", "B21P32.jpg"),
    ("238Z-3bbd8852", "B21P01.jpg"),
    ("239Z-0b09f3ae", "B21P26.jpg"),
    ("239Z-04e4745d", "B21P07.jpg"),
    ("240Z-7af49aa1", "B21P36.jpg"),
    ("241Z-7f810f0f", "B21P24.jpg"),
    ("242Z-abcd3e53", "B21P29.jpg"),
    ("243Z-4591b9b2", "B21P25.jpg"),
    ("244Z-0260225c", "B21P03.jpg"),
    ("244Z-13a93439", "B21P18.jpg"),
    ("245Z-92bc73db", "B21P22.jpg"),
    ("246Z-c4c13e66", "B21P23.jpg"),
    ("247Z-8d33af9e", "B21P19.jpg"),
    ("248Z-4d22ac35", "B21P12.jpg"),
    ("249Z-d8e26a50", "B21P13.jpg"),
    ("250Z-d76749ac", "B21P28.jpg"),
    ("250Z-c6e8ad64", "B21P33.jpg"),
    ("251Z-0c56db5c", "B21P08.jpg"),
    ("252Z-447856bf", "B21P14.jpg"),
    ("253Z-b8a7f464", "B21P10.jpg"),
    ("254Z-feaa2d78", "B21P05.jpg"),
    ("255Z-151f08e0", "B21P27.jpg"),
    ("255Z-85dcc798", "B21P04.jpg"),
    ("256Z-1e11f9c0", "B21P34.jpg"),
    ("257Z-90645155", "B21P31.jpg"),
    ("258Z-1f47e453", "B21P30.jpg"),
    ("259Z-79e870a7", "B21P06.jpg"),
    ("260Z-2788fb7e", "B21P17.jpg"),
    ("261Z-e416835a", "B21P02.jpg"),
    ("261Z-01d83728", "B21P15.jpg"),
    ("262Z-aa6e8720", "B21P16.jpg"),
    ("264Z-a26ea3cc", "B21P11.jpg"),
]

os.makedirs(DEST_IMAGES, exist_ok=True)

for stamp, name in B21:
    matches = [f for f in os.listdir(CLIP) if f.startswith(f"clipboard-2026-11-24T02-19-22-{stamp}") and f.endswith(".jpg")]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one clipboard file for {stamp}, got {matches}")
    shutil.copy2(os.path.join(CLIP, matches[0]), os.path.join(DEST_IMAGES, name))

b24 = sorted(f for f in os.listdir(SRC_B24) if f.lower().endswith(".jpg"))
for name in b24:
    shutil.copy2(os.path.join(SRC_B24, name), os.path.join(DEST_IMAGES, name))

print(f"Copied {len(B21)} B21 + {len(b24)} B24 = {len(B21) + len(b24)} images to {DEST_IMAGES}")
