#!/usr/bin/env python3
"""
Server-side PDF generator for Chronos Media Onboarding
This script can be called via a webhook or backend service to generate the complete onboarding PDF
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
import base64
import io
from PIL import Image as PILImage

def generate_onboarding_pdf(name, roles, email, date, signature_base64, output_filename):
    """
    Generate a complete onboarding PDF with all content from the packet
    
    Args:
        name: Full name of the person
        roles: List of roles (e.g., ['Live Team', 'Audio Team'])
        email: Email address
        date: Date string
        signature_base64: Base64 encoded signature image
        output_filename: Path where PDF should be saved
    """
    
    # Create PDF document
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#21B5FF'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2F6BFF'),
        spaceAfter=12,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#21B5FF'),
        spaceAfter=8,
        spaceBefore=12
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2F6BFF'),
        spaceAfter=6,
        spaceBefore=10
    )
    
    # Story (content) list
    story = []
    
    # PAGE 1 - Cover Page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("Welcome to Chronos Media", title_style))
    story.append(Paragraph("Capturing the Agapē Moments", subtitle_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Onboarding & Welcome Packet", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Chronos Media Live LLC", styles['Normal']))
    story.append(Paragraph("Professional Media • Live Streaming • Photography • Audio Production • Church Media", 
                          styles['Normal']))
    story.append(PageBreak())
    
    # PAGE 2 - Welcome & Getting Started
    story.append(Paragraph("Welcome", heading_style))
    story.append(Paragraph(
        "Welcome to Chronos Media. We're excited to have you join our team. Whether you are staff, "
        "contractor, or volunteer, you are an important part of our mission to serve moments that matter "
        "with excellence, care, and professionalism.",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Who We Are", heading_style))
    story.append(Paragraph(
        "Chronos Media Live LLC is a full-service media company specializing in live streaming, "
        "photography, audio production, and church-focused media services. Our name reflects "
        "preparation, reliability, and purpose — and our work reflects service.",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Our Services", heading_style))
    story.append(Paragraph("• <b>Live Streaming & Broadcast</b> (chronosmedia.to/live) – Multi-camera production and reliable streaming for churches and events.", styles['Normal']))
    story.append(Paragraph("• <b>Photography</b> (chronosmedia.to/photos) – Event and ministry photography that tells the story with clarity and respect.", styles['Normal']))
    story.append(Paragraph("• <b>Audio Production</b> (chronosmedia.to/audio) – Clean, balanced sound for live events and recordings.", styles['Normal']))
    story.append(Paragraph("• <b>Church Teams</b> (chronosmedia.to/churches) – Worship-aware production workflows and support.", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Communication & Tools", heading_style))
    story.append(Paragraph(
        "You will be provided a @chronosmedia.to email address. For initial setup, contact Stephen Johnson at media@chronosmedia.to.",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Getting Started Checklist", heading_style))
    story.append(Paragraph("✔ Email account activated (credentials received)", styles['Normal']))
    story.append(Paragraph("✔ Device(s) configured (phone and/or computer)", styles['Normal']))
    story.append(Paragraph("✔ Role and responsibilities reviewed", styles['Normal']))
    story.append(Paragraph("✔ Access to required tools/platforms confirmed", styles['Normal']))
    story.append(Paragraph("✔ Point of contact for your role established", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Support & Help", heading_style))
    story.append(Paragraph(
        "If you need help at any time, contact media@chronosmedia.to or call (267) 535-0921. "
        "During live events, follow on-site leadership and escalate issues calmly and clearly.",
        styles['Normal']
    ))
    story.append(PageBreak())
    
    # PAGE 3 - Role-Specific Guides
    story.append(Paragraph("Role-Specific Quick Guides", heading_style))
    story.append(Paragraph("Use the section that matches your assigned role. These are the standards we follow on every project.", styles['Normal']))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("Live Team (Streaming & Broadcast)", subheading_style))
    story.append(Paragraph("• <b>Arrive early:</b> target 60–90 minutes before call time (or as directed).", styles['Normal']))
    story.append(Paragraph("• <b>Pre-flight checks:</b> power, cables, audio levels, camera framing, and internet/encoder status.", styles['Normal']))
    story.append(Paragraph("• <b>During the live:</b> keep chatter minimal, monitor audio meters, and watch for dropped frames.", styles['Normal']))
    story.append(Paragraph("• <b>Red button rule:</b> when live, changes are coordinated through the lead only.", styles['Normal']))
    story.append(Paragraph("• <b>Wrap:</b> confirm recording saved, upload/hand-off files, pack down neatly, and leave the space better than you found it.", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("Photo Team (Photography)", subheading_style))
    story.append(Paragraph("• <b>Respect the moment:</b> be present but unobtrusive — especially in worship and prayer.", styles['Normal']))
    story.append(Paragraph("• <b>Consistency:</b> keep color/white balance stable across the set when possible.", styles['Normal']))
    story.append(Paragraph("• <b>Shot list:</b> confirm the must-have shots (leaders, key moments, groups, details).", styles['Normal']))
    story.append(Paragraph("• <b>File handling:</b> do not delete originals; back up promptly; name folders clearly (Date_Event_Client).", styles['Normal']))
    story.append(Paragraph("• <b>Delivery:</b> follow the approved workflow for selections, edits, and exports.", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("Audio Team (Live Sound & Recording)", subheading_style))
    story.append(Paragraph("• <b>Clarity first:</b> vocals must be intelligible; avoid harsh EQ; manage dynamics.", styles['Normal']))
    story.append(Paragraph("• <b>Feedback prevention:</b> gain staging, mic discipline, and smart EQ are your best tools.", styles['Normal']))
    story.append(Paragraph("• <b>Mic etiquette:</b> placement matters — ask before moving a mic, and tape cables safely.", styles['Normal']))
    story.append(Paragraph("• <b>Record when possible:</b> capture a safety recording for post needs (if approved).", styles['Normal']))
    story.append(Paragraph("• <b>Communication:</b> coordinate with Live/Photo leads for cues and quiet moments.", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("Church Teams (Worship & Ministry Environments)", subheading_style))
    story.append(Paragraph("• <b>Reverence:</b> worship spaces require extra care — move quietly and avoid distractions.", styles['Normal']))
    story.append(Paragraph("• <b>Privacy:</b> do not record or photograph private moments unless explicitly approved.", styles['Normal']))
    story.append(Paragraph("• <b>Service flow:</b> learn the order of service and confirm cues (prayer, communion, altar calls).", styles['Normal']))
    story.append(Paragraph("• <b>Dress & demeanor:</b> professional, modest, and aligned with the church's culture.", styles['Normal']))
    story.append(Paragraph("• <b>Kids & sensitive content:</b> follow client guidance and any consent requirements.", styles['Normal']))
    story.append(PageBreak())
    
    # PAGE 4 - Code of Conduct
    story.append(Paragraph("Code of Conduct", heading_style))
    story.append(Paragraph("• <b>Professionalism:</b> represent Chronos Media with respect, patience, and calm communication.", styles['Normal']))
    story.append(Paragraph("• <b>Confidentiality:</b> do not share client details, schedules, footage, or private information without approval.", styles['Normal']))
    story.append(Paragraph("• <b>Safety:</b> tape down cables, keep walkways clear, and follow venue rules at all times.", styles['Normal']))
    story.append(Paragraph("• <b>Respect property:</b> handle equipment carefully; report damage immediately; never leave gear unattended.", styles['Normal']))
    story.append(Paragraph("• <b>Social media:</b> do not post behind-the-scenes or client content unless you receive explicit permission.", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Dress Guidelines", heading_style))
    story.append(Paragraph("Dress depends on the venue, but always prioritize a clean, professional appearance. When unsure, dress more formally.", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    
    # Dress table
    dress_data = [
        ['Recommended', 'Avoid'],
        ['Black or neutral clothing; clean shoes', 'Graphic tees; loud patterns'],
        ['Business casual for churches/events', 'Shorts (unless approved for outdoor work)'],
        ['Modest attire for worship services', 'Distracting accessories/noisy jewelry'],
        ['Weather-ready layers for outdoor setups', 'Unprofessional hats (unless part of uniform)']
    ]
    
    dress_table = Table(dress_data, colWidths=[3*inch, 3*inch])
    dress_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E8F4F8')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(dress_table)
    story.append(PageBreak())
    
    # PAGE 5 - Church-Specific Guidelines
    story.append(Paragraph("Church-Specific Onboarding Insert", heading_style))
    story.append(Paragraph("This insert applies whenever Chronos Media serves a church service, ministry, or faith-based event.", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("• <b>Arrival & setup:</b> check in with the designated church point-of-contact before unloading.", styles['Normal']))
    story.append(Paragraph("• <b>Soundcheck:</b> confirm speaking mic(s), music inputs, and livestream feed levels.", styles['Normal']))
    story.append(Paragraph("• <b>Camera positions:</b> avoid blocking aisles; keep trip hazards minimized; confirm any restricted areas.", styles['Normal']))
    story.append(Paragraph("• <b>During prayer/altar calls:</b> reduce movement; zoom/crop respectfully; prioritize reverence.", styles['Normal']))
    story.append(Paragraph("• <b>Children/minors:</b> follow church guidance on filming/photography and consent requirements.", styles['Normal']))
    story.append(Paragraph("• <b>After service:</b> confirm any deliverables (recording link, photos, audio) and thank staff.", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("Quick Links", heading_style))
    story.append(Paragraph("Main Site: chronosmedia.to", styles['Normal']))
    story.append(Paragraph("Live: chronosmedia.to/live", styles['Normal']))
    story.append(Paragraph("Photos: chronosmedia.to/photos", styles['Normal']))
    story.append(Paragraph("Audio: chronosmedia.to/audio", styles['Normal']))
    story.append(Paragraph("Church Teams: chronosmedia.to/churches", styles['Normal']))
    story.append(PageBreak())
    
    # PAGE 6 - Acknowledgment (Filled Form)
    story.append(Paragraph("Acknowledgment", heading_style))
    story.append(Paragraph(
        "I confirm that I have received and reviewed the Chronos Media onboarding materials, including "
        "role expectations, code of conduct, and church-specific guidelines.",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Form data
    form_data = [
        ['Name (Print):', name],
        ['Role(s):', ', '.join(roles)],
        ['Email:', email],
        ['Date:', date]
    ]
    
    form_table = Table(form_data, colWidths=[1.5*inch, 4.5*inch])
    form_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(form_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Add signature
    story.append(Paragraph("<b>Signature:</b>", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    
    # Decode and add signature image
    if signature_base64:
        try:
            # Remove data URL prefix if present
            if ',' in signature_base64:
                signature_base64 = signature_base64.split(',')[1]
            
            # Decode base64
            signature_data = base64.b64decode(signature_base64)
            signature_img = PILImage.open(io.BytesIO(signature_data))
            
            # Save temporarily
            temp_sig_path = '/tmp/signature_temp.png'
            signature_img.save(temp_sig_path)
            
            # Add to PDF
            story.append(Image(temp_sig_path, width=3*inch, height=0.75*inch))
        except Exception as e:
            story.append(Paragraph(f"[Signature image error: {str(e)}]", styles['Italic']))
    
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "<i>Return this signed document to media@chronosmedia.to</i>",
        styles['Normal']
    ))
    
    # Build PDF
    doc.build(story)
    print(f"PDF generated successfully: {output_filename}")

# Example usage
if __name__ == "__main__":
    # Test data
    generate_onboarding_pdf(
        name="John Doe",
        roles=["Live Team", "Audio Team"],
        email="john.doe@example.com",
        date="2026-01-10",
        signature_base64="",  # Would contain actual base64 signature
        output_filename="/tmp/test_onboarding.pdf"
    )
