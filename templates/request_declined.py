from templates.images import LOGO_ICON_BLUE
from templates.images import LOGO_RED


def request_declined_template(user_package):
    return (f"""
                <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml"
                    xmlns:v="urn:schemas-microsoft-com:vml"
                    xmlns:o="urn:schemas-microsoft-com:office:office">
                    <head>
                    <!--[if gte mso 9]><xml>
                    <o:OfficeDocumentSettings>
                    <o:AllowPNG/>
                    <o:PixelsPerInch>96</o:PixelsPerInch>
                    </o:OfficeDocumentSettings>
                    </xml><![endif]-->
                    <title>PsyCare</title>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                    <meta name="viewport" content="width=device-width, initial-scale=1.0 " />
                    <meta name="format-detection" content="telephone=no"/>
                    <!--[if !mso]><!-->
                    <link href="https://fonts.googleapis.com/css?family=Lato:100,100i,300,300i,400,700,700i,900,900i" rel="stylesheet" />
                    <!--<![endif]-->
                    </head>
                    <body style="font-size: 15px;overflow-x:hidden;">
                        <div>
                            <div style="margin-top:20px;">
                                <img style="width:230px;" src="{LOGO_RED}"/>
                            </div>
                            <div style="margin-left:15px;">
                                <div style="margin-top:20px;font-size:20px;font-weight:900;">Hello {user_package['full_name']},</div>
                                <p style="padding: 5px 7.5px 7.5px 20px;line-height:25px;">
                                    We are sorry to inform you that your account request has been declined by our admission team.
                                    <br/>
                                    This decision may have been taken due to one or more of the following:
                                    <ul>
                                        <li>Lack of information to determine truthfulness of your certification as a therapist.</li>
                                        <li>Your clinic location is not supported by our platform.</li>
                                        <li>Invalid and/or explicit content.</li>
                                    </ul>
                                    <br/>
                                    If you disagree with the decision taken by our admission team, 
                                    feel free to reply to this email with further information or try 
                                    submitting another application at <a href="https://psycare.ca">psycare.ca</a>.
                                    <br/><br/>
                                    <b style="font-size:18px;">Thanks!</b>
                                </p>
                                <div style="display:flex;">
                                    <div style="margin-bottom:5px;">
                                        <img alt="PsyCare Logo" style="width:80px;" src="{LOGO_ICON_BLUE}"/>
                                    </div>
                                    <div style="margin-left:15px;margin-top:14px;">
                                        <div align="left" style="margin-bottom:5px;">
                                            <span style="font-weight:900;font-size:19px;">PsyCare Info Team</span>
                                        </div>
                                        <div>
                                            <div style="display:flex; justify-content:flex-start">
                                                <div style="margin-right:7.5px;">
                                                    <a style="color:#9fa8da;" href="https://psycare.ca">psycare.ca</a>
                                                </div>
                                                <div style="margin-right:7.5px;">|</div>
                                                <div style="margin-right:7.5px;">
                                                    <a style="color:#9fa8da;" href="https://fb.me/psycareorg">Facebook</a>
                                                </div>
                                                <div style="margin-right:7.5px;">|</div>
                                                <div style="margin-right:7.5px;">
                                                    <a href="https://www.linkedin.com/company/psycare-org">
                                                        LinkedIn
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>    
                    </body>
                </html>"""
            )
