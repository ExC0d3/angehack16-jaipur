'use strict';

const api_key = 'key-78152fd286ccb1147c5a4ee898de3f7d';

const domain = 'buildahack.com';

export const mailgun = require('mailgun-js')({apiKey:api_key, domain:domain});

const Campaign_Name = 'My campaign';
const User = {
	name: 'Manoj Pandey'
};

export const mailDetails = {
	from: `Abhinav <abhinav@buildahack.com>`,
	to:`manojpandey1996@gmail.com`,
	subject: 'Campaining Update',
	text:'Hey, keeping you posted with the update in my Campaingn. Glad to be working with you'
}


