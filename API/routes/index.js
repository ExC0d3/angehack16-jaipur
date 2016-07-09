'use strict';

import {mailgun, mailDetails} from '../services/email';
import {client} from '../services/sms';
var express = require('express');
var router = express.Router();


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });

});

router.get('/promote/email',(req,res,next) => {
	///TODO - Add user details in req query

	mailgun.messages().send(mailDetails)
	.then((data) => {
		res.send({
			result:'sucess',
			reason:null
		});
	})
	.catch((err) => {
		res.send({
			result:'failed',
			reason:err
		});
	}) 
});

router.get('/promote/sms',(req,res,next) => {
	///TODO - user details from query parameters

	client.sendMessage({
		to:'+919910089606',
		from:'+14136422080',
		body:'Hello from a friend'
	}, (err, data) => {
		if (err)
			res.send({
				result:'fail',
				reasons:err
			});
		else
			res.send({
				result:'success',
				reason:null
			});
	});
});

module.exports = router;
