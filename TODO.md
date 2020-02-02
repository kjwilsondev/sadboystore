# TODO

## User

- id [Integer]
- email (unique) [String]
  - blog updates (Mailchimp, Mandrill)
- phone number [Integer]
  - shipping updates (Twilio)
- address [String]
- closet [Array]
  - array of item.id
- cart [Array]
  - array of item.id

### Fuctions

Email Reciept

- Send User Form to Mailchimp
- Import template from Mailchimp
- Send User Form Mandrill
