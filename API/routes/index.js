'use strict';

import {mailgun, mailDetails} from '../services/email';
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

module.exports = router;
