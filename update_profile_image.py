#!/usr/bin/env python3
"""
Script to help update the profile image for Jiarong Guo's website.
This script provides instructions for processing the profile photo.
"""

import os
from PIL import Image
import sys

def process_profile_image(input_path, output_path="/workspace/images/profile.png"):
    """
    Process the profile image to create a suitable avatar.
    
    Args:
        input_path: Path to the input image
        output_path: Path where the processed image should be saved
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Create a square crop from the center
            width, height = img.size
            size = min(width, height)
            
            # Calculate crop coordinates (center crop)
            left = (width - size) // 2
            top = (height - size) // 2
            right = left + size
            bottom = top + size
            
            # Crop to square
            img_cropped = img.crop((left, top, right, bottom))
            
            # Resize to 300x300 for high quality
            img_resized = img_cropped.resize((300, 300), Image.Resampling.LANCZOS)
            
            # Save as PNG
            img_resized.save(output_path, "PNG", quality=95)
            
            print(f"✅ Profile image processed successfully!")
            print(f"   Input: {input_path}")
            print(f"   Output: {output_path}")
            print(f"   Size: 300x300 pixels")
            
    except Exception as e:
        print(f"❌ Error processing image: {e}")
        return False
    
    return True

def main():
    print("🖼️  Profile Image Processor for Jiarong Guo's Website")
    print("=" * 50)
    
    # Check if input image is provided
    if len(sys.argv) < 2:
        print("Usage: python update_profile_image.py <input_image_path>")
        print("\nInstructions:")
        print("1. Save your profile photo as 'new_profile.jpg' in the current directory")
        print("2. Run: python update_profile_image.py new_profile.jpg")
        print("3. The script will create a 300x300 square crop and save it as profile.png")
        return
    
    input_path = sys.argv[1]
    
    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        return
    
    # Process the image
    success = process_profile_image(input_path)
    
    if success:
        print("\n🎉 Profile image updated successfully!")
        print("   The new profile.png is ready to use on your website.")
    else:
        print("\n💡 Manual instructions:")
        print("1. Open your photo in an image editor (GIMP, Photoshop, or online tools)")
        print("2. Crop it to a square (1:1 aspect ratio)")
        print("3. Resize to 300x300 pixels")
        print("4. Save as PNG format")
        print("5. Replace /workspace/images/profile.png with your processed image")

if __name__ == "__main__":
    main()