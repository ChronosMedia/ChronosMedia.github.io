# Onboarding Form - Troubleshooting Guide

## Issue: Signature and PDF Generation Not Working

If the signature pad and PDF generation aren't working, try these solutions:

### Solution 1: Use the Simplified Version

I've created **two working test versions** in the package:

1. **onboarding-test.html** - Minimal test version with console logging
2. **onboarding-simple.html** - Clean, simplified version with all features

**To test:**
1. Open `onboarding-simple.html` in your browser
2. Try drawing a signature
3. Fill out the form
4. Click "Submit & Generate PDF"
5. Check your browser console (F12) for any errors

### Solution 2: Common Issues & Fixes

#### Issue: Signature not drawing
**Causes:**
- JavaScript not fully loaded
- Canvas context not initialized
- Browser security settings

**Fix:**
- Open browser console (F12) and check for errors
- Try the simplified version first
- Make sure JavaScript is enabled

#### Issue: PDF not generating
**Causes:**
- jsPDF library not loaded
- Browser blocking file downloads
- JavaScript error before PDF generation

**Fix:**
1. Check browser console for errors
2. Make sure pop-ups/downloads aren't blocked
3. Try in a different browser (Chrome recommended)

#### Issue: Form submit button does nothing
**Causes:**
- Form validation failing
- No roles selected
- JavaScript error

**Fix:**
1. Open browser console (F12)
2. Select at least one role
3. Fill all required fields
4. Look for error messages in console

### Solution 3: Browser Compatibility

**Recommended browsers:**
- Google Chrome (latest)
- Mozilla Firefox (latest)
- Microsoft Edge (latest)
- Safari (latest)

**Not recommended:**
- Internet Explorer (not supported)
- Very old browser versions

### Solution 4: Local Testing

If you're testing locally (file:// protocol), some features may not work due to browser security:

1. Use a local web server instead:
   ```bash
   # Python 3
   python3 -m http.server 8000
   
   # Then open: http://localhost:8000/onboarding-simple.html
   ```

2. Or upload to your actual website and test there

### Solution 5: Check Browser Console

Open Developer Tools (F12) and look for errors:

**Common errors and solutions:**

1. **"jsPDF is not defined"**
   - Solution: CDN blocked or slow internet. Refresh page.

2. **"Cannot read property 'getContext' of null"**
   - Solution: Canvas element not found. Check HTML.

3. **"Failed to execute 'toDataURL' on 'HTMLCanvasElement'"**
   - Solution: Canvas not initialized properly. Use simplified version.

### Files to Test

In order of simplicity:

1. **onboarding-test.html** - Bare bones with logging (TEST THIS FIRST)
2. **onboarding-simple.html** - Clean working version
3. **onboarding.html** - Full styled version

### Still Not Working?

If none of the versions work:

1. Check browser console for specific error
2. Try a different browser
3. Test on actual web server (not file://)
4. Send console error message to support

### Contact

If you continue having issues:
- Email: media@chronosmedia.to
- Include: Browser version, console errors, which file you tested

## Quick Test Steps

1. Open `onboarding-test.html`
2. Open browser console (F12)
3. Try drawing on signature pad
4. Look for "Started drawing" message in console
5. Fill form and submit
6. Watch console for "PDF saved" message
7. Check downloads folder for PDF

If test version works but main version doesn't, there may be a CSS or JavaScript conflict in the styled version.
