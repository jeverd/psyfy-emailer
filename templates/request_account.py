def request_account_template(user_package):
    return (
        """
            <html>
                <body style="font-size: 20px;overflow-x:hidden;">
                    <div style="background: url(https://raw.githubusercontent.com/lnogueir/psyfy-frontend/master/psyfy/src/assets/main_background.jpg);
                                height:35px; 
                                width: 100%;
                                padding: 20px 20px 31px 20px;
                                ">
                        <img src="https://raw.githubusercontent.com/lnogueir/psyfy-frontend/master/psyfy/src/assets/images/psycare_logo.png" 
                        style="height: 47.5px"/>   
                    </div>
                    <div>
                        <p style="padding: 5px 7.5px 7.5px 20px;">
                            <span style="margin:0;font-size:22px;font-weight:900;">Hello {0},</span>
                            <ul>
                                <li>Name: {0} <br/></li>
                                <li>Email: {1}</li>
                                <li>Contact Number: {2}</li>
                                <li>Clinic Address: {3}</li>
                                <li>About: {4}</li>
                            </ul>
                            <span style="margin:0;font-size:22px;font-weight:900;">Hello {0},</span>
                            <ol>
                                <li><a href="{5}">Accept</a></li>
                                <li><a href="{6}">Deny</a></li>
                            </ol>
                        </p>
                        <div>
                            <i>PsyCare info team.</i>
                        </div>
                    </div>
                </body>
            </html>
			""".format(
            user_package['full_name'],
            user_package['contact_email'],
            user_package['phone_number'],
            user_package['address'],
            user_package['about'],
            user_package['accept'],
            user_package['deny']
        )
    )
