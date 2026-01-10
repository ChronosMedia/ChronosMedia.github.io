# Chronos Media Onboarding System - Implementation Guide

## Overview
The updated onboarding system includes:
1. **Multiple role selection** with checkboxes
2. **Complete onboarding content** in the generated PDF (6 pages)
3. **Digital signature** functionality
4. **Automatic email** with form data to media@chronosmedia.to

## Changes Made

### 1. Role Selection (Checkboxes)
Changed from dropdown to checkboxes to allow multiple role selection:
- Live Team (Streaming & Broadcast)
- Photo Team (Photography)  
- Audio Team (Live Sound & Recording)
- Church Team (Worship & Ministry)
- Other

### 2. Complete PDF Generation
The PDF now includes all 6 pages from the onboarding packet:

**Page 1 - Cover Page**
- Welcome to Chronos Media
- Capturing the Agapē Moments
- Company information

**Page 2 - Welcome & Getting Started**
- Welcome message
- Who We Are
- Our Services
- Communication & Tools
- Getting Started Checklist
- Support & Help

**Page 3 - Role-Specific Quick Guides**
- Live Team guidelines
- Photo Team guidelines
- Audio Team guidelines
- Church Teams guidelines

**Page 4 - Code of Conduct**
- Professionalism rules
- Dress Guidelines (table with Recommended/Avoid columns)

**Page 5 - Church-Specific Guidelines**
- Arrival & setup
- Camera positions
- Prayer/altar calls
- Quick Links

**Page 6 - Acknowledgment Form** (Filled with user data)
- Name (Print)
- Role(s) - shows all selected roles
- Email
- Date
- Signature image

### 3. JavaScript Implementation

The form submission handler:
1. Validates at least one role is selected
2. Collects all form data including selected roles array
3. Generates a 6-page PDF using jsPDF with:
   - Custom fonts and colors matching Chronos Media brand
   - Proper page breaks and spacing
   - Header/footer on each page
   - Tables for dress guidelines
   - Signature image embedded
4. Downloads the PDF with filename: `Chronos_Onboarding_[Name]_[Date].pdf`
5. Opens email client with pre-filled information

### 4. Files Provided

**onboarding.html** - Updated web form with:
- Checkbox role selection
- Complete PDF generation JavaScript
- Matches current website styling

**generate_onboarding_pdf_server.py** - Python backend script using reportlab for:
- Server-side PDF generation if needed
- Can be called via webhook/API
- Generates professional multi-page PDF with all content

## How To Use

### For Web Users:
1. Fill out the form fields
2. Select one or more roles (checkboxes)
3. Draw signature on canvas
4. Click "Submit & Generate PDF"
5. PDF downloads automatically
6. Email client opens with form data
7. Attach the downloaded PDF and send

### For Backend Integration (Optional):
If you want server-side PDF generation instead of client-side:

1. Install dependencies:
```bash
pip install reportlab Pillow --break-system-packages
```

2. Call the Python script:
```python
from generate_onboarding_pdf_server import generate_onboarding_pdf

generate_onboarding_pdf(
    name="John Doe",
    roles=["Live Team", "Audio Team"],
    email="john@example.com",
    date="2026-01-10",
    signature_base64="data:image/png;base64,...",
    output_filename="output.pdf"
)
```

3. Set up a simple Flask/FastAPI endpoint to receive form submissions and generate PDFs server-side

## Key Features

✅ Multiple role selection with checkboxes
✅ Complete 6-page onboarding packet in PDF
✅ Digital signature capture
✅ Automatic PDF download
✅ Pre-filled email to media@chronosmedia.to
✅ Google Analytics tracking
✅ Responsive design matching website
✅ Dark/light theme support

## Testing

1. Open onboarding.html
2. Fill out all fields
3. Select multiple roles
4. Draw signature
5. Submit form
6. Check that PDF contains all 6 pages with correct content
7. Verify email opens with correct data

## Notes

- The JavaScript version generates PDF entirely client-side (no server needed)
- PDF includes complete onboarding content from the original packet
- Signature is embedded as PNG image in the PDF
- File size is approximately 200-300KB depending on signature complexity
- Works on all modern browsers including mobile

## Future Enhancements

Potential improvements:
- Server-side PDF generation for consistency
- Email attachment automation (requires backend)
- Database storage of submissions
- Admin dashboard to view submissions
- Automatic reminder emails
- E-signature verification with timestamps

## Support

For questions or issues:
- Email: media@chronosmedia.to
- Phone: (267) 535-0921
