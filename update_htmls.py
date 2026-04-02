import os
import re

# Highly specific and premium Unsplash image IDs that match the distinct cyber/tech vibe
service_data = {
    "vapt.html": {
        "title": "Vulnerability Assessment & Penetration Testing (VAPT)",
        "desc": "Expert VAPT services to identify, analyze, and mitigate cyber threats before they are exploited. Comprehensive vulnerability assessment and penetration testing.",
        "img": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "Our Vulnerability Assessment and Penetration Testing (VAPT) methodology combines the precision of automated scanning with the depth of manual expert analysis. We don't just find bugs; we evaluate the business risk of every vulnerability discovered.",
        "features": [
            "<strong>Web Application Security:</strong> In-depth testing based on OWASP Top 10, covering injection flaws, broken authentication, and sensitive data exposure.",
            "<strong>Network Penetration Testing:</strong> Auditing internal and external network infrastructure to identify exploitable services and weak configurations.",
            "<strong>API Security Audits:</strong> Comprehensive testing of RESTful and GraphQL APIs for logic flaws, authorization issues, and data leaks.",
            "<strong>Mobile App VAPT:</strong> Analyzing Android and iOS applications for client-side vulnerabilities, insecure storage, and communication flaws."
        ],
        "process": "Our process begins with detailed reconnaissance and threat modeling. We سپس execute controlled exploitation to confirm vulnerabilities, followed by providing a comprehensive report with prioritized remediation steps and a debriefing session with your technical team."
    },
    "red-teaming.html": {
        "title": "Red Teaming Operations",
        "desc": "Simulated real-world cyber attacks to test your organization's detection and response capabilities. Advanced red teaming services by cybersecurity experts.",
        "img": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "Unlike a standard pentest, Red Teaming is a full-scope multi-layered attack simulation designed to measure how well your people, networks, applications, and physical security controls can withstand a real-world motivated attacker.",
        "features": [
            "<strong>Adversary Simulation:</strong> Mimicking the TTPs (Tactics, Techniques, and Procedures) of known Advanced Persistent Threat (APT) groups.",
            "<strong>Social Engineering:</strong> Testing the 'human firewall' through targeted phishing, vishing, and physical tailgating simulations.",
            "<strong>Physical Security Testing:</strong> Evaluating the security of physical premises, including lock picking, badge cloning, and unauthorized entry attempts.",
            "<strong>Command & Control (C2):</strong> Establishing covert communication channels to simulate data exfiltration and persistent network presence."
        ],
        "process": "We operate in stealth mode over an extended period. The objective is not just to 'get in', but to stay undetected and achieve specific crown-jewel objectives, providing a true test of your SOC's detection and response speed."
    },
    "digital-forensics.html": {
        "title": "Digital Forensics & Incident Response",
        "desc": "Rapid incident response and deep digital forensics to investigate cyber breaches, recover data, and secure your infrastructure against future attacks.",
        "img": "https://images.unsplash.com/photo-1614064641936-3899884d24f0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "In the aftermath of a breach, every second counts. Our Digital Forensics and Incident Response (DFIR) team provides clinical-grade investigation services to identify the root cause, quantify the damage, and secure evidence for legal or regulatory requirements.",
        "features": [
            "<strong>Compromise Assessment:</strong> Rapidly determining if your network has already been breached and identifying the extent of the infection.",
            "<strong>Memory & Disk Forensics:</strong> Deep analysis of volatile memory and storage media to recover deleted files, chat logs, and malware artifacts.",
            "<strong>Network Traffic Analysis:</strong> Reconstructing packet data to identify exfiltrated data and trace the attacker's lateral movement.",
            "<strong>Malware Reverse Engineering:</strong> Deconstructing malicious binaries to understand their functionality, C2 infrastructure, and kill switch."
        ],
        "process": "We follow a strict chain-of-custody protocol. From initial triage and evidence preservation to deep-dive analysis and final reporting, we ensure that our findings are scientifically sound and legally defensible."
    },
    "source-code-review.html": {
        "title": "Secure Source Code Review",
        "desc": "In-depth secure source code review to identify hidden vulnerabilities, logic flaws, and backend security loopholes in your application's architecture.",
        "img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "Security starts at the line of code. Our Secure Source Code Review service identifies vulnerabilities that automated tools often miss, focusing on business logic flaws, insecure cryptographic implementations, and hidden backdoors.",
        "features": [
            "<strong>Static Analysis (SAST):</strong> Automated scanning paired with manual line-by-line review of codebase in Java, Python, Go, PHP, and JavaScript.",
            "<strong>Logic Flow Mapping:</strong> Analyzing how data flows through the application to find bypasses in authentication and authorization modules.",
            "<strong>Dependency Auditing:</strong> Checking third-party libraries and frameworks for known vulnerabilities and insecure supply chain risks.",
            "<strong>Secure Coding Training:</strong> Providing your development team with actionable feedback to prevent future security regression."
        ],
        "process": "We integrate with your CI/CD pipeline or perform a standalone audit. Every finding is accompanied by a code snippet demonstrating the fix, ensuring your developers can implement remediations immediately."
    },
    "web-development.html": {
        "title": "Full Stack Web Development",
        "desc": "High-performance, scalable, and secure full-stack web development services. Custom web applications tailored to your business needs.",
        "img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "We build web applications that are as secure as they are beautiful. Our development philosophy centers on high performance, SEO optimization, and a 'security-by-design' approach, ensuring your platform is ready for global scale.",
        "features": [
            "<strong>Modern Frontend Engineering:</strong> Interactive and responsive interfaces built with React, Next.js, and high-quality CSS/Tailwind designs.",
            "<strong>Robust Backend Architecture:</strong> Scalable server-side logic using Node.js, Go, or Python with secure API design and microservices.",
            "<strong>Database Optimization:</strong> High-efficiency data modeling with PostgreSQL, MongoDB, or MySQL, optimized for query speed and data integrity.",
            "<strong>Cloud-Native Deployment:</strong> Expert setup on AWS, GCP, or Azure with Docker, Kubernetes, and automated CI/CD pipelines."
        ],
        "process": "From wireframing and UI/UX design to backend development and security hardening, we follow an agile methodology to deliver high-quality code in rapid cycles."
    },
    "application-development.html": {
        "title": "Application Development",
        "desc": "Cross-platform mobile and desktop application development crafting intuitive, high-performance, and secure digital experiences.",
        "img": "https://images.unsplash.com/photo-1526498460520-4c246339dccb?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "We develop high-performance applications that provide a seamless experience across all platforms. Whether it's a mobile app for millions or a specialized desktop tool for enterprise security, we deliver precision-engineered software.",
        "features": [
            "<strong>Cross-Platform Mobile:</strong> Single-codebase development using Flutter and React Native for beautiful, high-performance iOS and Android apps.",
            "<strong>Native Desktop Apps:</strong> Powerful applications for Windows, macOS, and Linux built using Electron, C++, and Python frameworks.",
            "<strong>Offline-First Design:</strong> Implementing local data persistence and synchronization to ensure apps remain functional in low-connectivity environments.",
            "<strong>Security Obfuscation:</strong> Advanced code hardening and runtime protection to prevent reverse engineering and unauthorized app modification."
        ],
        "process": "Our development cycle emphasizes user testing and performance profiling. We ensure your application is bug-free, lightning-fast, and ready for distribution on the App Store or Google Play."
    },
    "training-certification.html": {
        "title": "Training & Certification",
        "desc": "Professional cybersecurity training and certification. Equip your team with the knowledge to defend against modern cyber operations.",
        "img": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "Knowledge is the ultimate defense. Our training programs are designed by active cybersecurity operators to bridge the gap between academic theory and real-world cyber battlefields, equipping professionals with tactical skills.",
        "features": [
            "<strong>Cert-Oriented Training:</strong> In-depth preparation for top-tier certifications like OSCP, CEH, and CISSP with hands-on lab environments.",
            "<strong>Custom Corporate Workshops:</strong> Tailored security awareness training for employees and specialized technical training for IT teams.",
            "<strong>Hands-On Cyber Range:</strong> Interactive labs where students can practice attacking and defending real-world network architectures.",
            "<strong>Adversary Mindset:</strong> Teaching the 'Think Like a Hacker' philosophy to help defenders anticipate and neutralize threats before they manifest."
        ],
        "process": "We provide a blended learning experience combining live instructional sessions with lifetime access to our proprietary lab environments and updated course materials."
    },
    "soc.html": {
        "title": "Security Operation Center (SOC)",
        "desc": "24/7 Security Operation Center (SOC) services. Continuous monitoring, threat detection, and rapid incident response to secure your digital assets.",
        "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "Our Security Operation Center (SOC) acts as your organization's digital immune system. We provide 24/7/365 vigilance, leveraging AI-powered threat detection and elite security analysts to neutralize threats in real-time.",
        "features": [
            "<strong>SIEM/SOAR Integration:</strong> Centralized log management and automated incident response workflows to reduce MTTR (Mean Time to Respond).",
            "<strong>Threat Hunting:</strong> Proactively searching through network and endpoint telemetry to find hidden threats that bypassed traditional security tools.",
            "<strong>Endpoint Detection & Response (EDR):</strong> Continuous monitoring of all network endpoints to detect and block malicious process behavior.",
            "<strong>Dark Web Monitoring:</strong> Tracking hacker forums and leak sites to identify if your organization's credentials or data are being traded."
        ],
        "process": "We establish a seamless connection with your infrastructure, monitor alerts around the clock, and provide immediate containment actions when a high-priority threat is detected."
    },
    "data-recovery.html": {
        "title": "Advanced Data Recovery",
        "desc": "Professional data recovery services to restore lost, corrupted, or ransomware-encrypted critical business information and digital assets.",
        "img": "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "Data loss can be catastrophic. Our Advanced Data Recovery laboratory specializes in recovering data from physically damaged drives, corrupted file systems, and complex ransomware encryption scenarios where others have failed.",
        "features": [
            "<strong>Ransomware Decryption:</strong> Specialized techniques to recover data encrypted by modern locker and wiper ransomware strains.",
            "<strong>Forensic Image Recovery:</strong> Carving data from formatted or partially overwritten drives using deep-sector forensic analysis.",
            "<strong>SQL & Database Repair:</strong> Restoring corrupted database files (MDF, LDF, ODB) and recovering lost records from complex transactional logs.",
            "<strong>Cloud Data Recovery:</strong> Recovering accidentally deleted or lost data from SaaS platforms and cloud storage environments."
        ],
        "process": "We begin with a non-destructive assessment of the media. Once the recovery feasibility is determined, we perform sector-level cloning and use forensic tools to extract your data into a secure, encrypted retrieval drive."
    },
    "it-audit.html": {
        "title": "IT Infrastructure Audit",
        "desc": "Comprehensive IT Infrastructure Audits to evaluate your network architecture, identify weaknesses, and ensure optimal security posture.",
        "img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "An IT audit is the foundation of a healthy technical ecosystem. We perform a granular review of your network architecture, cloud configurations, and hardware assets to ensure they are optimized for performance and security.",
        "features": [
            "<strong>Network Topology Review:</strong> Auditing firewall rules, VLAN segmentation, and routing protocols to ensure a zero-trust architecture.",
            "<strong>Active Directory Audit:</strong> Evaluating AD group policies, permission inheritance, and stale accounts to prevent privilege escalation.",
            "<strong>Cloud Configuration Audit:</strong> Benchmarking your AWS, Azure, or GCP environment against CIS (Center for Internet Security) best practices.",
            "<strong>Asset Inventory & Management:</strong> Identifying shadow IT and ensuring all hardware assets are mapped, patched, and accounted for."
        ],
        "process": "Our audit results in a prioritized roadmap of technical improvements, ranging from immediate security patches to long-term architectural re-engineering."
    },
    "compliance-audit.html": {
        "title": "Regulatory Compliance & Audit",
        "desc": "Ensuring your business meets global cybersecurity standards like ISO 27001, SOC2, and HIPAA through rigorous compliance auditing.",
        "img": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "Regulatory compliance is no longer optional. We navigate the complex landscape of global data protection laws to ensure your organization remains compliant, avoiding heavy fines and reputational damage.",
        "features": [
            "<strong>ISO 27001 Readiness:</strong> Preparing your Information Security Management System (ISMS) for international certification.",
            "<strong>SOC2 & HIPAA Audits:</strong> Specialized auditing for service providers and healthcare organizations to protect sensitive client data.",
            "<strong>GDPR & Data Privacy:</strong> Ensuring your data handling practices align with European and international privacy regulations.",
            "<strong>PCI-DSS Compliance:</strong> Hardening your payment processing infrastructure to meet the strict standards of the credit card industry."
        ],
        "process": "We perform a thorough gap analysis of your current controls, provide a detailed remediation plan, and conduct a final audit to certify your compliance status."
    },
    "corporate-fraud-investigation.html": {
        "title": "Corporate Fraud & Insider Threat Investigation",
        "desc": "Expert investigation services to detect corporate fraud, identify insider threats, and secure evidence for legal proceedings.",
        "img": "https://images.unsplash.com/photo-1453723490680-7b64c0345151?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "long_desc": "Trust but verify. When corporate integrity is at stake, our forensic investigators provide the technical expertise to uncover the truth behind complex fraud schemes and internal security breaches.",
        "features": [
            "<strong>Economic Crime Analysis:</strong> Tracing illicit financial flows and identifying misappropriation of corporate assets using forensic techniques.",
            "<strong>Insider Threat Detection:</strong> Monitoring for data exfiltration, unauthorized access, and sabotage by disgruntled or compromised employees.",
            "<strong>Digital Evidence Recovery:</strong> Extracting forensic artifacts from mobile phones, laptops, and company servers to prove fraudulent activity.",
            "<strong>Expert Witness Testimony:</strong> Providing scientifically sound evidence and expert testimony for legal proceedings and corporate tribunals."
        ],
        "process": "All investigations are conducted with the highest level of confidentiality and technical precision, ensuring that collected evidence remains admissible in a court of law."
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
          const res = await fetch("/.netlify/functions/send-inquiry", {
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
          status.innerText = "Fatal Error: Comm Link Offline or Server Unavailable.";
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

    # Clean up previous injections
    content = re.sub(r'<!-- Cyber 3D Styles.*?-->[\s\S]*?</style>', '', content)
    content = re.sub(r'<!-- 3D Particles Container -->[\s\S]*?</body>', '</body>', content)
    content = re.sub(r'<!-- Inquiry Modal -->[\s\S]*?</body>', '</body>', content)
    content = re.sub(r'<div class="tilt-box".*?</div>', '', content, flags=re.DOTALL)
    content = content.replace('<div class="blob-service"></div>', '')

    # Clean up duplicate <head> closing injections
    content = re.sub(r'(</head>\s*)+', '</head>\n', content)
    content = re.sub(r'(</body>\s*)+', '</body>\n', content)

    svc_title = data['title']
    svc_desc = data['desc']
    svc_img = data['img']
    svc_long_desc = data['long_desc']
    svc_features = data['features']
    svc_process = data['process']
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

    # Better H1 match
    h1_match = re.search(r'<h1>\s*&#60;(.*?)/?&#62;\s*</h1>', content, flags=re.DOTALL)
    if h1_match:
        service_name = h1_match.group(1).strip()
        if service_name.endswith('/'):
            service_name = service_name[:-1].strip()

        # Update the button
        btn_pattern = r'(<a\s+href="mailto:[^"]*"\s+class="letsTalkBtn"[\s\S]*?</a>)|(<div[^>]*position:\s*relative[^>]*>[\s\S]*?<button[^>]*letsTalkBtn[\s\S]*?</button>\s*</div>(?:</div>)?)'
        
        def replace_btn(match):
            return f'''<div style="position: relative; z-index: 100; margin-top: 50px; text-align: center;">
            <button type="button" class="letsTalkBtn inq-btn" data-service="{service_name}" style="border: none; cursor: pointer; background: transparent; padding: 0; outline: none;">
          <div class="letsTalkBtn-text" style="color: #00f2fe; text-shadow: 0 0 10px rgba(0,242,254,0.5); font-family: 'Orbitron', sans-serif; font-weight: bold; letter-spacing: 1px; z-index: 10; position: relative; padding: 15px 30px;">Inquire About Service</div>
          <span class="letsTalkBtn-BG" style="background: rgba(0,242,254,0.1); border: 1px solid #00f2fe; border-radius: 5px;"></span>
        </button></div>'''
        
        content = re.sub(btn_pattern, replace_btn, content)
        
        # Add 3D Tilt Image
        img_html = f'''
        <div class="tilt-box" data-aos="zoom-in" data-aos-duration="1000">
          <img src="{svc_img}" alt="{service_name}" style="width: 100%; height: 350px; object-fit: cover; display: block; filter: brightness(0.8) contrast(1.2);">
        </div>
        '''
        
        h1_full = h1_match.group(0)
        content = content.replace(h1_full, h1_full + img_html)

        # Inject Riches Content (Long Desc, Features, Process)
        # We replace the placeholders or existing content
        features_html = ""
        for feature in svc_features:
            features_html += f"<li>{feature}</li>\n"
        
        rich_content = f'''
        <p data-aos="fade-up">{svc_long_desc}</p>
        <h2 data-aos="fade-up">Core Specialties:</h2>
        <ul data-aos="fade-up">
            {features_html}
        </ul>
        <h2 data-aos="fade-up">The Process:</h2>
        <p data-aos="fade-up">{svc_process}</p>
        '''

        # We look for the first <p> after the tilt-box (which is after h1)
        # Actually it's easier to just replace everything between tilt-box and button
        # But we don't know the exact structure of each file.
        # Let's try to find the <h2>Core Specialties:</h2> and replace around it.
        
        content = re.sub(r'<p>.*?</p>\s*<h2>Core Specialties:</h2>[\s\S]*?<h2>The Process:</h2>\s*<p>.*?</p>', rich_content, content, flags=re.DOTALL)
            
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Injected Riches Content, Modals, 3D Images to all service pages successfully.")
