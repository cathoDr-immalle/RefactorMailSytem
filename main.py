 if __name__ == '__main__':
    s = MailServer()
    
    print(" Logging in Joske to mail server...")
    c1 = MailClient(s, "Joske")

    print(" User joske sending mail to Jantje...")
    c1.sendMailItem("Jantje", "Hello!!!")

    print(" Logging in Jantje to mail server...")
    c2 = MailClient(s, "Jantje")

    print(" User Jantje reading mail...")
    c2.printNextMailItem()

    print(" User Jantje reading mail...")
    c2.printNextMailItem()
