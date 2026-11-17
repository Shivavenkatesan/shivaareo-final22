AERO PRIME MED - LAUNCH STEPS (Hostinger)
1. On your computer, in this folder run:
     python3 set-domain.py yourdomain.com info@yourdomain.com
   (fills canonicals, sitemap, robots, contact form recipient, privacy/terms email)
2. With internet on, run:  python3 download-images.py
   (copies the catalogue photos from the other website into assets/images/catalogue/)
3. Upload ALL files (including hidden .htaccess) into public_html via Hostinger File Manager.
4. hPanel > Emails: create the mailbox you used above (e.g. info@yourdomain.com) and a noreply@yourdomain.com
   mailbox or forwarder. contact.php sends from noreply@ - it must exist on your domain.
5. hPanel > Security > SSL: activate free SSL (the .htaccess then forces https + www).
6. Send a test enquiry from /contact.html and confirm it arrives. Check spam folder once.
7. Google Search Console: add the site, submit https://www.yourdomain.com/sitemap.xml.
Still your responsibility: confirm product range, specs and compliance wording before publishing;
add your phone/address on the Contact page if you want them shown.
