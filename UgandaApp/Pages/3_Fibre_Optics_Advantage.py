import streamlit as st 


col1, col2 = st.columns([2, 1])  # Create two equal-width columns

# Fill the first column  
col1.header("                    ")
col1.header("                    ")
col1.header("                    ")
col1.markdown("<h1 style='color: #fcdc04;'>Solution Overview</h1>", unsafe_allow_html=True)

# Place the image in the second column
col2.image("logo2.png", width=300)




st.markdown("<h3 style='color: #9ca69c;'>Fiber optics offers several advantages over traditional methods of data transmission, such as copper wiring. Here are some key advantages of fiber optics:</h3>", unsafe_allow_html=True)
st.info('''# Advantages of Fiber Optics:

1. High Bandwidth             |   4. Immunity to Electromagnetic Interference
   - Enables transmission of         - Unaffected by electromagnetic interference
     large amounts of data             and radio frequency interference
   - Ideal for high-speed              (EMI/RFI)
     internet, video streaming,      - Can be installed near electrical equipment
     cloud computing, etc.

2. Fast Data Transmission     |    5. Secure Data Transmission
   - Light travels at high            - Difficult to tap into transmission without
     speeds through fiber optic        detection
     cables                            - Highly secure for sensitive applications
   - Achieves terabit-per-second       - Used for government communications,
     speeds                            banking transactions, medical data transfer

3. Long-Distance Transmission     6. Lightweight and Compact
   - Minimal signal degradation       - Lightweight and smaller diameter compared
     over long distances               to copper wires
   - Connects geographically          - Easier installation and management
     distant locations                 - Higher density and efficient use of resources

7. Resistance to Environmental Factors
   - Less susceptible to temperature fluctuations,
     moisture, and corrosion
   - Suitable for underwater, underground,
     and industrial settings
''')

