/**
 * What the forms say when something needs fixing, and after a contact message is sent. The design has no words for
 * these; the wording follows corelith.co.zw's own forms.
 */
export const FORM_MESSAGES: Record<string, string> = {
  name: "Please tell us your name.",
  school: "Please tell us the name of your school.",
  phone: "Please give us a phone number so we can call to arrange the demo.",
  email: "Please enter a valid email address.",
  message: "Please write your message.",
  busy: "That's a few submissions in a row. Give it a minute, or email hello@corelith.co.zw.",
  failed: "We couldn't save your request just now. Please email hello@corelith.co.zw and we'll pick it up directly.",
  sent: "Sent. We read every message and reply by email.",
};
