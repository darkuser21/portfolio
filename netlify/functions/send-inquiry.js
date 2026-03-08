const nodemailer = require("nodemailer");

exports.handler = async (event, context) => {
  // Only allow POST requests
  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: "Method Not Allowed" }),
    };
  }

  try {
    const { name, number, email, service, message } = JSON.parse(event.body);

    const serviceType = service || "General/Portfolio Inquiry";

    if (!name || !number || !email) {
      return {
        statusCode: 400,
        body: JSON.stringify({
          error: "Missing required fields (Name, Number, or Email)",
        }),
      };
    }

    const ADMIN_EMAIL = process.env.EMAIL_USER;
    const EMAIL_USER = process.env.EMAIL_USER;
    const APP_PASSWORD = process.env.APP_PASSWORD;

    const transporter = nodemailer.createTransport({
      service: "gmail",
      auth: {
        user: EMAIL_USER,
        pass: APP_PASSWORD,
      },
    });

    const cyberStyle = `
      <style>
        body { font-family: 'Courier New', monospace; background-color: #0d0d12; color: #e0e0e0; margin: 0; padding: 20px; }
        .container { max-width: 600px; margin: 0 auto; background: #13131c; border: 1px solid #00c3ff; border-radius: 8px; overflow: hidden; box-shadow: 0 0 15px rgba(0, 195, 255, 0.2); }
        .header { background: #00c3ff; color: #000; padding: 20px; text-align: center; font-family: 'Arial', sans-serif; text-transform: uppercase; font-weight: bold; letter-spacing: 2px; }
        .content { padding: 30px; }
        .footer { text-align: center; padding: 15px; font-size: 12px; color: #777; border-top: 1px solid #333; }
        h2 { color: #00c3ff; margin-top: 0; }
        p { line-height: 1.6; }
        .field-label { color: #8ac8ff; font-weight: bold; }
        .data-box { background: rgba(0, 195, 255, 0.05); border-left: 3px solid #00c3ff; padding: 10px 15px; margin: 15px 0; }
      </style>
    `;

    // 1. Email to Admin
    const mailToAdmin = {
      from: `"Inquiry System" <${EMAIL_USER}>`,
      to: ADMIN_EMAIL,
      subject: `New Inquiry: ${serviceType} - from ${name}`,
      html: `
        <html>
        <head>${cyberStyle}</head>
        <body>
          <div class="container">
            <div class="header">
              <h3>New Service Inquiry</h3>
            </div>
            <div class="content">
              <h2>Inquiry From: ${name}</h2>
              <div class="data-box">
                <p><span class="field-label">Service Required:</span> ${serviceType}</p>
                <p><span class="field-label">Contact Number:</span> ${number}</p>
                <p><span class="field-label">Email Address:</span> ${email}</p>
              </div>
              <p><span class="field-label">Message Details:</span></p>
              <div class="data-box" style="border-left-color: #ff5555;">
                <p>${message || "No additional message provided."}</p>
              </div>
            </div>
            <div class="footer">
              Automated message from Sanny Prajapati's Portfolio System
            </div>
          </div>
        </body>
        </html>
      `,
    };

    // 2. Auto-reply Confirmation to User
    const mailToUser = {
      from: `"Sanny Prajapati Contact" <${EMAIL_USER}>`,
      to: email,
      subject: `Confirmation: Inquiry Received regarding ${serviceType}`,
      html: `
        <html>
        <head>${cyberStyle}</head>
        <body>
          <div class="container">
            <div class="header" style="background: #2563eb; color: #fff;">
              <h3>Inquiry Received Successfully</h3>
            </div>
            <div class="content">
              <h2>Dear ${name},</h2>
              <p>Thank you for reaching out. We have successfully received your inquiry regarding:</p>
              <div class="data-box" style="border-left-color: #2563eb;">
                <p><span class="field-label">Requested Service:</span> ${serviceType}</p>
              </div>
              <p>I will carefully review your message and get back to you shortly at the contact details you provided (${number} / ${email}).</p>
              <br/>
              <p>Best regards,</p>
              <p style="color: #00c3ff; font-weight: bold; font-family: 'Arial', sans-serif;">Sanny Prajapati</p>
              <p style="font-size: 13px; color: #aaa;">Cyber Security Consultant & Developer</p>
            </div>
            <div class="footer">
              This is an automated confirmation email. Please do not reply directly to this message.
            </div>
          </div>
        </body>
        </html>
      `,
    };

    await Promise.all([
      transporter.sendMail(mailToAdmin),
      transporter.sendMail(mailToUser),
    ]);

    return {
      statusCode: 200,
      body: JSON.stringify({
        success: true,
        message: "Emails sent successfully",
      }),
    };
  } catch (error) {
    console.error("Error sending email:", error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: "Failed to send emails." }),
    };
  }
};
