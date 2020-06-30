import pandas as pd
import datetime
import smtplib  # To send emails

# Enter your details
GMAIL_ID = ""
GMAIL_PASS = ""


def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")
    # SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP server
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PASS)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub} and message {msg}")
    s.quit()


if __name__ == "__main__":
    df = pd.read_excel(r"data.xlsx")
    today = datetime.datetime.now()
    today = today.strftime("%d-%m")  # Print as date(%d)-month(%m)
    yearNow = datetime.datetime.now().strftime("%Y")
    # print(type(today))
    writeInd = []

    # for Iterations in the df
    for index, item in df.iterrows():  # item is for columns
        bday = item['Birthday'].strftime("%d-%m")
        if today == bday and yearNow not in str(item['Year']):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)

    if len(writeInd) == 0:
        pass
    else:
        for i in writeInd:
            yr = df.loc[i, 'Year']
            print(yr)
            df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)
            print(df.loc[i, 'Year'])

        df.to_excel('data.xlsx', index=False)