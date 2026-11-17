<?php
// Aero Prime Med enquiry handler. Run set-domain.py (or edit these two lines).
$TO   = 'info@YOURDOMAIN.COM';
$FROM = 'noreply@YOURDOMAIN.COM'; // must be an email on your Hostinger domain
if ($_SERVER['REQUEST_METHOD'] !== 'POST' || !empty($_POST['website'])) { header('Location: contact.html'); exit; }
function f($k,$n=3000){ return trim(substr(str_replace(["\r","\n"],' ',(string)($_POST[$k] ?? '')),0,$n)); }
function m($k,$n=3000){ return trim(substr((string)($_POST[$k] ?? ''),0,$n)); }
$company=f('company',120); $name=f('name',100); $email=f('email',120); $phone=f('phone',40); $country=f('country',80);
$products=m('products'); $message=m('message');
if (!$company || !$name || !filter_var($email,FILTER_VALIDATE_EMAIL) || !$country || !$products) { header('Location: contact.html?error=1#enquiry'); exit; }
$body="Company: $company\nName: $name\nEmail: $email\nPhone: $phone\nCountry: $country\n\nProducts & quantities:\n$products\n\nDetails:\n$message\n";
$headers="From: Aero Prime Med Website <$FROM>\r\nReply-To: $email\r\nContent-Type: text/plain; charset=UTF-8";
$ok=mail($TO,'New website enquiry from '.$company,$body,$headers);
header('Location: contact.html?'.($ok?'sent=1':'error=1').'#enquiry'); exit;
