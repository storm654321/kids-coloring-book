---
name: kids-coloring-book
description: Converts photos, anime scenes, pet pictures, or drawings into clean, kid-friendly black-and-white coloring book pages using multimodal image generation (Nano Banana / Imagen / DALL-E).
---

# Kids Coloring Book Maker

This skill enables the AI assistant to act as a professional coloring-book illustrator and converter. It takes any user-provided reference image (cartoons, video game screenshots, family photos, pet pictures) and transforms it into an outline-only coloring page optimized for young children.

## When to Activate
Activate this skill whenever the user says:
- "Make a coloring page from this image"
- "Turn this photo/screenshot into a coloring book page"
- "幫我把這張圖改造成小朋友可以著色的版本"
- "把這張照片變成著色本/線稿"

## Key Transformation Rules for Kids Coloring Pages
Young children require specific line art characteristics for an enjoyable coloring experience:
1. **Bold & Closed Outlines**: Lines must be clear, crisp, and closed so colors don't bleed visually.
2. **Pure White Fills (Zero Shading)**: No gradients, no soft shadows, no grayscale textures, and no halftone screentones.
3. **Appropriate Simplicity**: Simplify noisy textures (like fur, ground gravel, complex cloth folds) while strictly preserving recognizable character features and expressions.
4. **Print-Friendly Format**: Default to standard 16:9 or 4:3 landscape / portrait suitable for instant A4 printing.

## Prompt Engineering Formula
When invoking `generate_image` or instructing an image model:

```text
Transform this image into a children's coloring book page.
Black and white line art with bold, clear outlines and pure white fills.
No shading, no grayscale, no color, no halftone dots.
The scene features [Describe main characters, their actions and expressions],
[Describe foreground objects], and [Simplified background elements].
Cute, clear, closed contours, and easy to color for young children.
```

## Post-Processing & Printable Output
1. Provide color suggestions for kids (identifying key character colors).
2. Offer printing tips (A4 Landscape/Portrait fit-to-page).
3. If applicable, run `scripts/export_a4_pdf.py` to compile the image into a clean printable PDF.
