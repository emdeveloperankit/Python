from fpdf import FPDF

def generate_business_guide_pdf(file_name='bus.pdf'):
    # Create a PDF instance
    pdf = FPDF()
    pdf.add_page()
    
    # Set font
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, txt="How to Start a Business as a Solo Entrepreneur", ln=True, align='C')
    pdf.ln(10)
    
    # Content
    content = [
        {"title": "1. Find Your Business Idea", 
         "text": """
    Identify a niche that aligns with your skills and interests. Research market demand, competition, 
    and target audience to validate your business idea.
         """},
         
        {"title": "2. Write a Business Plan",
         "text": """
    Draft a business plan outlining your goals, target market, pricing strategy, financial projections, 
    and marketing strategy. This will serve as your roadmap to success.
         """},

        {"title": "3. Choose a Business Structure",
         "text": """
    Decide whether to register as a sole proprietorship, LLC, or another business structure. Each type has 
    different legal and tax implications, so choose wisely.
         """},

        {"title": "4. Register Your Business",
         "text": """
    Register your business name and obtain the necessary licenses and permits. Check local, state, and federal 
    requirements to ensure compliance.
         """},

        {"title": "5. Set Up a Business Bank Account",
         "text": """
    Open a separate business bank account to manage your finances efficiently. This will help keep personal 
    and business expenses separate.
         """},

        {"title": "6. Build an Online Presence",
         "text": """
    Create a professional website and set up social media profiles to reach a broader audience. Consider 
    investing in digital marketing and SEO to attract customers.
         """},

        {"title": "7. Network and Collaborate",
         "text": """
    Join industry-specific groups, attend networking events, and collaborate with other entrepreneurs to 
    build relationships and grow your business.
         """},

        {"title": "8. Focus on Customer Service",
         "text": """
    Provide excellent customer service to build trust and loyalty. Happy customers are likely to recommend 
    your business to others.
         """},

        {"title": "9. Manage Finances Effectively",
         "text": """
    Track your expenses, profits, and cash flow. Consider using accounting software to streamline your 
    financial management.
         """},

        {"title": "10. Stay Adaptable",
         "text": """
    Be prepared to adapt to changes in the market. Continuously learn and improve your skills to stay 
    competitive.
         """}
    ]

    # Add sections to the PDF
    for section in content:
        pdf.set_font("Arial", style='B', size=14)
        pdf.cell(200, 10, txt=section["title"], ln=True)
        
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, section["text"])
        pdf.ln(5)
    
    # Save the PDF
    pdf.output(file_name)
    print(f"PDF generated successfully: {file_name}")

# Run the function to generate the PDF
generate_business_guide_pdf()
