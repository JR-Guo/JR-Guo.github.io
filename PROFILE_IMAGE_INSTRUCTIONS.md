# Profile Image Update Instructions

## Overview
Your website layout has been fixed! Now you need to update your profile image based on the photo you provided.

## Current Status
- ✅ Layout issues fixed
- ✅ Duplicate content removed
- ✅ Clean structure implemented
- ⏳ Profile image needs updating

## How to Update Your Profile Image

### Option 1: Using the Python Script (Recommended)
1. Save your profile photo as `new_profile.jpg` in the `/workspace` directory
2. Run the script:
   ```bash
   cd /workspace
   python3 update_profile_image.py new_profile.jpg
   ```
3. The script will automatically:
   - Crop the image to a square
   - Resize to 300x300 pixels
   - Save as `profile.png` in the correct location

### Option 2: Manual Processing
1. Open your photo in any image editor (GIMP, Photoshop, Canva, etc.)
2. Crop to a square (1:1 aspect ratio) - focus on your face/upper body
3. Resize to 300x300 pixels
4. Save as PNG format
5. Replace `/workspace/images/profile.png` with your processed image

### Image Requirements
- **Format**: PNG (preferred) or JPG
- **Size**: 300x300 pixels (square)
- **Quality**: High resolution for crisp display
- **Content**: Professional headshot, centered

## Layout Improvements Made

### ✅ Fixed Issues
1. **Removed duplicate content** - No more redundant profile sections
2. **Cleaned up structure** - Streamlined the homepage layout
3. **Improved organization** - Better content hierarchy
4. **Maintained functionality** - All features still work

### ✅ Current Layout Structure
```
Header (with overlay image and call-to-action buttons)
↓
Author Profile Section (with your photo and bio)
↓
Highlights Section (Publications, Talks, Global Map)
↓
Latest Blog Posts
```

## Next Steps
1. Update your profile image using one of the methods above
2. Test the website to ensure everything looks good
3. The layout is now clean and professional!

## Technical Notes
- The profile image is referenced in `_config.yml` as `author.avatar: "profile.png"`
- The image is displayed in the `author-profile.html` include
- CSS styling is handled in `_sass/_sidebar.scss`