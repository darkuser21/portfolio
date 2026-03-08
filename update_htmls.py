import os
import re

# Highly specific and premium Unsplash image IDs that match the distinct cyber/tech vibe
service_data = {
    "vapt.html": {
        "title": "Vulnerability Assessment & Penetration Testing (VAPT)",
        "desc": "Expert VAPT services to identify, analyze, and mitigate cyber threats before they are exploited. Comprehensive vulnerability assessment and penetration testing.",
        "img": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    },
    "red-teaming.html": {
        "title": "Red Teaming Operations",
        "desc": "Simulated real-world cyber attacks to test your organization's detection and response capabilities. Advanced red teaming services by cybersecurity experts.",
        "img": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    },
    "digital-forensics.html": {
        "title": "Digital Forensics & Incident Response",
        "desc": "Rapid incident response and deep digital forensics to investigate cyber breaches, recover data, and secure your infrastructure against future attacks.",
        "img": "https://images.unsplash.com/photo-1614064641936-3899884d24f0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    },
    "source-code-review.html": {
        "title": "Secure Source Code Review",
        "desc": "In-depth secure source code review to identify hidden vulnerabilities, logic flaws, and backend security loopholes in your application's architecture.",
        "img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    },
    "web-development.html": {
        "title": "Full Stack Web Development",
        "desc": "High-performance, scalable, and secure full-stack web development services. Custom web applications tailored to your business needs.",
        "img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    },
    "application-development.html": {
        "title": "Application Development",
        "desc": "Cross-platform mobile and desktop application development crafting intuitive, high-performance, and secure digital experiences.",
        "img": "https://images.unsplash.com/photo-1526498460520-4c246339dccb?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    },
    "training-certification.html": {
        "title": "Training & Certification",
        "desc": "Professional cybersecurity training and certification. Equip your team with the knowledge to defend against modern cyber operations.",
        "img": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    },
    "soc.html": {
        "title": "Security Operation Center (SOC)",
        "desc": "24/7 Security Operation Center (SOC) services. Continuous monitoring, threat detection, and rapid incident response to secure your digital assets.",
        "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    },
    "data-recovery.html": {
        "title": "Advanced Data Recovery",
        "desc": "Professional data recovery services to restore lost, corrupted, or ransomware-encrypted critical business information and digital assets.",
        "img": "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    },
    "it-audit.html": {
        "title": "IT Infrastructure Audit",
        "desc": "Comprehensive IT Infrastructure Audits to evaluate your network architecture, identify weaknesses, and ensure optimal security posture.",
        "img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    },
    "compliance-audit.html": {
        "title": "Compliance & ISMS Audit",
        "desc": "ISO 27001, GDPR, and ISMS compliance auditing to ensure your organization meets all regulatory cybersecurity requirements.",
        "img": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    },
    "corporate-fraud-investigation.html": {
        "title": "Corporate Fraud Investigation",
        "desc": "Discreet and advanced corporate fraud investigations utilizing digital forensics to uncover financial irregularities and insider threats.",
        "img": "https://images.unsplash.com/photo-1618044733300-9472054094ee?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
    }
}

base_dir = r"c:\Users\DELL\Desktop\Projects\MY WEB\portfolio"

modal_css = """
  <!-- Cyber 3D Styles & Particles -->
  <style>
    body { background-color: #050508 !important; }
    #tsparticles {
      position: fixed; width: 100%; height: 100vh; top: 0; left: 0; z-index: -2;
    }
    .blob-service {
      position: fixed; right: -15%; top: -10%; background-color: #00f2fe; width: 700px; height: 100vh;
      filter: blur(250px); opacity: 0.15; animation: breath-service 6s ease-in-out infinite alternate; z-index: -1; pointer-events: none;
    }
    @keyframes breath-service { 0% {opacity: 0.1; transform: scale(0.9) translate(0, 0);} 100% {opacity: 0.25; transform: scale(1.1) translate(-50px, 50px);} }

    /* 3D Image Container */
    .tilt-box {
      border-radius: 12px; overflow: hidden; box-shadow: 0 15px 40px rgba(0,242,254,0.15);
      position: relative; margin: 40px 0 50px 0; border: 1px solid rgba(0, 242, 254, 0.3);
      background: #000;
      width: 100%; height: auto;
    }
    .tilt-box img {
      width: 100%; height: 400px; object-fit: cover; display: block; filter: brightness(0.85) contrast(1.1) saturate(1.2);
    }
    .tilt-box::after {
        content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(135deg, rgba(0,242,254,0.2) 0%, transparent 50%, rgba(255,81,47,0.1) 100%); pointer-events: none; mix-blend-mode: overlay;
    }

    /* Modal Styles */
    .modal {
      display: none; position: fixed; z-index: 9999; left: 0; top: 0;
      width: 100%; height: 100%; overflow: auto;
      background-color: rgba(0,0,5,0.9); backdrop-filter: blur(15px);
    }
    .modal-content {
      background: rgba(10, 10, 15, 0.95);
      margin: 8% auto; padding: 40px;
      border: 1px solid rgba(0,242,254,0.5); border-radius: 8px;
      width: 90%; max-width: 550px; position: relative;
      box-shadow: 0 0 40px rgba(0, 242, 254, 0.1), inset 0 0 20px rgba(0, 242, 254, 0.05);
      animation: modalFadeIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .modal-content::before {
      content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #00f2fe, #4facfe, #00f2fe);
      background-size: 200% 100%; animation: gradientShift 3s ease infinite; border-radius: 8px 8px 0 0;
    }
    @keyframes gradientShift { 0% {background-position: 100% 0;} 100% {background-position: -100% 0;} }
    @keyframes modalFadeIn {
      from {opacity: 0; transform: scale(0.8) translateY(30px);}
      to {opacity: 1; transform: scale(1) translateY(0);}
    }
    .close-btn { color: #555; float: right; font-size: 32px; font-weight: bold; cursor: pointer; transition: 0.3s; line-height: 20px; text-shadow: none; }
    .close-btn:hover { color: #ff512f; text-shadow: 0 0 15px #ff512f; transform: scale(1.1); }
    
    .form-group { margin-bottom: 25px; position: relative; }
    .form-group label { display: block; margin-bottom: 8px; color: #00f2fe; font-family: 'Fira Code', monospace; font-size: 0.85rem; letter-spacing: 1px; text-transform: uppercase;}
    .form-input {
      width: 100%; padding: 15px;
      background: rgba(0,0,0,0.6); border: 1px solid rgba(0,242,254,0.2);
      color: #fff; border-radius: 4px; font-family: 'Fira Code', monospace; font-size: 1rem;
      transition: all 0.3s ease; box-sizing: border-box;
    }
    .form-input::placeholder { color: rgba(255,255,255,0.2); }
    .form-input:focus { outline: none; border-color: #00f2fe; box-shadow: 0 0 20px rgba(0,242,254,0.2), inset 0 0 10px rgba(0,242,254,0.1); background: rgba(0,242,254,0.05); }
    
    .submit-btn {
      width: 100%; padding: 18px; border: none; cursor: pointer; margin-top: 15px;
      background: linear-gradient(90deg, #00f2fe, #4facfe); color: #000; font-weight: 900; letter-spacing: 2px;
      font-family: 'Orbitron', sans-serif; font-size: 1.2rem; border-radius: 4px;
      transition: all 0.3s ease; box-shadow: 0 0 20px rgba(0, 242, 254, 0.4); text-transform: uppercase;
      position: relative; overflow: hidden;
    }
    .submit-btn::before {
      content: ''; position: absolute; top: 0; left: -100%; width: 50%; height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
      transform: skewX(-25deg); transition: 0.5s;
    }
    .submit-btn:hover::before { left: 150%; }
    .submit-btn:hover { transform: translateY(-3px); box-shadow: 0 10px 30px rgba(0, 242, 254, 0.6); color: #fff; text-shadow: 0 0 5px rgba(255,255,255,0.5); }
    
    .form-status { margin-top: 20px; text-align: center; font-family: 'Fira Code', monospace; font-size: 0.95rem; text-shadow: 0 0 10px currentColor; font-weight: bold; }
    
    /* Cyber frame styling for images */
    .cyber-frame {
      position: absolute; pointer-events: none; width: 30px; height: 30px; border: 2px solid #00f2fe; z-index: 10;
    }
    .cf-tl { top: 15px; left: 15px; border-right: none; border-bottom: none; }
    .cf-tr { top: 15px; right: 15px; border-left: none; border-bottom: none; }
    .cf-bl { bottom: 15px; left: 15px; border-right: none; border-top: none; }
    .cf-br { bottom: 15px; right: 15px; border-left: none; border-top: none; }

    /* Mobile Responsive Queries */
    @media (max-width: 768px) {
      .modal-content {
        margin: 15% auto;
        padding: 25px 20px;
        width: 95%;
      }
      .modal-content h2 {
        font-size: 1.3rem;
        margin-bottom: 25px;
      }
      .submit-btn {
        padding: 15px;
        font-size: 1rem;
        letter-spacing: 1px;
      }
      .tilt-box img {
        height: 250px;
      }
      .blob-service {
        width: 100%;
        right: 0;
      }
      .close-btn {
        font-size: 28px;
        line-height: 15px;
      }
      .form-group {
        margin-bottom: 15px;
      }
      .form-input {
        padding: 12px;
      }
    }
  </style>
"""

modal_html = """
  <!-- 3D Particles Container -->
  <div id="tsparticles"></div>

  <!-- Inquiry Modal -->
  <div id="inquiryModal" class="modal">
    <div class="modal-content">
      <span class="close-btn">&times;</span>
      <h2 style="font-family: 'Orbitron', sans-serif; color: #fff; margin-bottom: 35px; text-shadow: 0 0 10px #00f2fe; letter-spacing: 2px;">
        Service Inquiry
      </h2>
      
      <form id="inquiryForm">
        <div class="form-group">
          <label>Full Name</label>
          <input type="text" id="inqName" class="form-input" placeholder="Enter your full name..." required />
        </div>
        <div class="form-group">
          <label>Contact Number</label>
          <input type="tel" id="inqNumber" class="form-input" placeholder="Enter your phone number..." required />
        </div>
        <div class="form-group">
          <label>Email Address</label>
          <input type="email" id="inqEmail" class="form-input" placeholder="Enter your email address..." required />
        </div>
        <div class="form-group">
          <label>Service of Interest</label>
          <input type="text" id="inqService" class="form-input" style="color: #fff; font-weight: bold; background: rgba(0,242,254,0.1); border-color: #00f2fe; text-shadow: 0 0 5px rgba(0,242,254,0.8);" readonly />
        </div>
        <div class="form-group">
          <label>Message / Details</label>
          <textarea id="inqMessage" class="form-input" placeholder="Explain your requirements here..." rows="4" style="resize: vertical;"></textarea>
        </div>
        <button type="submit" class="submit-btn" id="inqSubmitBtn">Submit Inquiry</button>
      </form>
      <div id="inqStatus" class="form-status"></div>
    </div>
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.8.0/vanilla-tilt.min.js"></script>
  <!-- tsParticles Library -->
  <script src="https://cdn.jsdelivr.net/npm/tsparticles-preset-triangles@2.11.0/tsparticles.preset.triangles.bundle.min.js"></script>
  
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      // Initialize 3D Particles
      try {
        tsParticles.load("tsparticles", {
          preset: "triangles",
          particles: {
            number: { value: 60, density: { enable: true, value_area: 800 } },
            color: { value: ["#00f2fe", "#4facfe"] },
            links: { enable: true, color: "#00f2fe", opacity: 0.2, distance: 150 },
            move: { enable: true, speed: 1.5, direction: "none", random: false, straight: false, outModes: "out" },
            size: { value: 2 },
            opacity: { value: 0.4, animation: { enable: true, speed: 1, minimumValue: 0.1 } }
          },
          interactivity: {
            events: {
              onHover: { enable: true, mode: "grab" },
              onClick: { enable: true, mode: "push" }
            },
            modes: { grab: { distance: 140, links: { opacity: 0.8 } }, push: { quantity: 4 } }
          },
          background: { color: "transparent" }
        });
      } catch(err) { console.error("tsParticles failed to load:", err); }
    });
  </script>

  <script>
    document.addEventListener("DOMContentLoaded", () => {
      // 3D Tilt initialization for non-mobile devices
      try {
        if(window.innerWidth > 768) {
          VanillaTilt.init(document.querySelectorAll(".tilt-box"), {
            max: 6,
            speed: 400,
            glare: true,
            "max-glare": 0.25,
            scale: 1.03
          });
        }
      } catch(e) {}

      // Modal Script
      const modal = document.getElementById("inquiryModal");
      const closeBtn = document.querySelector(".close-btn");
      const inqService = document.getElementById("inqService");
      const inqBtns = document.querySelectorAll(".inq-btn");

      inqBtns.forEach(btn => {
        btn.addEventListener("click", (e) => {
          e.preventDefault();
          const serviceName = btn.getAttribute("data-service");
          inqService.value = serviceName;
          modal.style.display = "block";
        });
      });

      closeBtn.onclick = () => { modal.style.display = "none"; document.getElementById("inqStatus").innerText = ""; }
      window.onclick = (e) => { if (e.target == modal) { modal.style.display = "none"; document.getElementById("inqStatus").innerText = ""; } }

      document.getElementById("inquiryForm").addEventListener("submit", async (e) => {
        e.preventDefault();
        const status = document.getElementById("inqStatus");
        const submitBtn = document.getElementById("inqSubmitBtn");
        
        status.style.color = "#00f2fe";
        status.innerText = "Submitting request...";
        submitBtn.disabled = true;
        submitBtn.innerText = "Processing...";
        
        const data = {
          name: document.getElementById("inqName").value,
          number: document.getElementById("inqNumber").value,
          email: document.getElementById("inqEmail").value,
          service: document.getElementById("inqService").value,
          message: document.getElementById("inqMessage").value
        };
        
        try {
          const res = await fetch("http://localhost:3000/send-inquiry", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
          });
          
          if(res.ok) {
            status.style.color = "#38ef7d";
            status.innerText = "Success! Your inquiry has been submitted and a confirmation email has been sent.";
            document.getElementById("inquiryForm").reset();
            setTimeout(() => {
                modal.style.display = "none";
                status.innerText = "";
            }, 3000);
          } else {
            status.style.color = "#ff512f";
            status.innerText = "Error: Our server failed to process the request.";
          }
        } catch (err) {
          status.style.color = "#ff512f";
          status.innerText = "Fatal Error: Ensure the Node.js backend is running on port 3000.";
        }
        
        submitBtn.disabled = false;
        submitBtn.innerText = "Submit Inquiry";
      });
    });
  </script>
"""

# Read and process files
for file, data in service_data.items():
    path = os.path.join(base_dir, file)
    if not os.path.exists(path):
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean up old tags first
    content = re.sub(r'<title>.*?</title>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<meta[^>]*name="description"[^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<!-- Advanced SEO.*?-->[\s\S]*?<!-- End Advanced SEO -->', '', content, flags=re.IGNORECASE)

    # Clean up previous injections by looking for unique identifiers to strictly not duplicate
    content = re.sub(r'<!-- Cyber 3D Styles.*?-->[\s\S]*?</style>', '', content)
    content = re.sub(r'<!-- 3D Particles Container -->[\s\S]*?</body>', '</body>', content)
    content = re.sub(r'<!-- Inquiry Modal -->[\s\S]*?</body>', '</body>', content)
    content = re.sub(r'<div class="tilt-box".*?</div>', '', content, flags=re.DOTALL)
    content = content.replace('<div class="blob-service"></div>', '')
    content = content.replace('<div class="blob"></div>', '') # if accidentally added bare blob

    # Clean up duplicate <head> closing injections just in case
    content = re.sub(r'(</head>\s*)+', '</head>\n', content)
    content = re.sub(r'(</body>\s*)+', '</body>\n', content)

    svc_title = data['title']
    svc_desc = data['desc']
    svc_img = data['img']
    canonical_url = f"https://darkuser.tech/{file}"

    seo_block = f"""
    <!-- Advanced SEO & Structured Data -->
    <title>{svc_title} | Sanny Prajapati</title>
    <meta name="description" content="{svc_desc}" />
    <link rel="canonical" href="{canonical_url}" />

    <!-- Open Graph Meta Tags -->
    <meta property="og:type" content="website" />
    <meta property="og:title" content="{svc_title} | Sanny Prajapati" />
    <meta property="og:description" content="{svc_desc}" />
    <meta property="og:image" content="{svc_img}" />
    <meta property="og:url" content="{canonical_url}" />
    <meta property="og:site_name" content="Sanny Prajapati Portfolio" />

    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:site" content="@Portfolio" />
    <meta name="twitter:title" content="{svc_title} | Sanny Prajapati" />
    <meta name="twitter:description" content="{svc_desc}" />
    <meta name="twitter:image" content="{svc_img}" />

    <!-- JSON-LD Schema Markup -->
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "{svc_title}",
        "description": "{svc_desc}",
        "provider": {{
          "@type": "Person",
          "name": "Sanny Prajapati"
        }},
        "serviceType": "Cybersecurity & Software Development",
        "areaServed": {{
          "@type": "Country",
          "name": "Global"
        }},
        "url": "{canonical_url}"
      }}
    </script>
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://darkuser.tech/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "Services",
            "item": "https://darkuser.tech/services.html"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "{svc_title}",
            "item": "{canonical_url}"
          }}
        ]
      }}
    </script>
    <!-- End Advanced SEO -->
    """

    # Inject SEO & Cyber CSS
    content = content.replace("</head>", f"{seo_block}\n{modal_css}\n</head>")

    # Inject Modal HTML & Script
    content = content.replace("</body>", f"{modal_html}\n</body>")
    
    # Inject Blob
    content = content.replace("<main>", "<main>\n    <div class=\"blob-service\"></div>")

    # Better H1 match bypassing whitespace
    # Example format: <h1>\n          &#60;Vulnerability Assessment & Penetration Testing (VAPT)/&#62;\n        </h1>
    # We want to match all text between &#60; and /&#62; inside the h1 tag.
    h1_match = re.search(r'<h1>\s*&#60;(.*?)/?&#62;\s*</h1>', content, flags=re.DOTALL)
    if h1_match:
        # For VAPT, raw extracted string might be `Vulnerability Assessment & Penetration Testing (VAPT)/`
        # Because we only have /? at the end, so let's strip any trailing /
        service_name = h1_match.group(1).strip()
        if service_name.endswith('/'):
            service_name = service_name[:-1].strip()

        # Update the button. We match any <a> letsTalkBtn or <div ...><button letsTalkBtn...
        btn_pattern = r'(<a\s+href="mailto:[^"]*"\s+class="letsTalkBtn"[\s\S]*?</a>)|(<div[^>]*position:\s*relative[^>]*>[\s\S]*?<button[^>]*letsTalkBtn[\s\S]*?</button>\s*</div>(?:</div>)?)'
        
        def replace_btn(match):
            return f'''<div style="position: relative; z-index: 100; margin-top: 20px;">
            <button type="button" class="letsTalkBtn inq-btn" data-service="{service_name}" style="border: none; cursor: pointer; background: transparent; padding: 0;">
          <div class="letsTalkBtn-text" style="color: #00f2fe; text-shadow: 0 0 10px rgba(0,242,254,0.5); font-family: 'Orbitron', sans-serif; font-weight: bold; letter-spacing: 1px; z-index: 10; position: relative; padding: 15px 30px;">Inquire About Service</div>
          <span class="letsTalkBtn-BG" style="background: rgba(0,242,254,0.1); border: 1px solid #00f2fe; border-radius: 5px;"></span>
        </button></div>'''
        
        content = re.sub(btn_pattern, replace_btn, content)
        
        # Add 3D Tilt Image right below the h1 block
        img_url = data['img']
        img_html = f'''
        <div class="tilt-box" data-aos="zoom-in" data-aos-duration="1000">
          <img src="{img_url}" alt="{service_name}" style="width: 100%; height: 350px; object-fit: cover; display: block; filter: brightness(0.8) contrast(1.2);">
        </div>
        '''
        
        # We replace the h1 itself with h1 + the image box
        h1_full = h1_match.group(0)
        content = content.replace(h1_full, h1_full + img_html)
            
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Injected Modals, 3D Images, and Backgrounds to all service pages successfully.")
