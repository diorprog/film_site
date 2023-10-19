<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    // Create email content
    $to = "your_email@example.com"; // Replace with your email address
    $subject = "Contact Form Submission";
    $headers = "From: $email";
    $message_body = "Name: $name\n";
    $message_body .= "Email: $email\n\n";
    $message_body .= "Message:\n$message";

    // Send email
    if (mail($to, $subject, $message_body, $headers)) {
        // Email sent successfully
        echo "Thank you for your message. We will get back to you shortly.";
    } else {
        // Error sending email
        echo "Sorry, there was an error sending your message. Please try again later.";
    }
} else {
    // Invalid request method
    echo "Invalid request method.";
}
?>
