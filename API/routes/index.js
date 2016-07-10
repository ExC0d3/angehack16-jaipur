'use strict';

import {mailgun, mailDetails} from '../services/email';
import {client} from '../services/sms';
import {plotly} from '../services/plot';


var fs = require('fs'); 
var express = require('express');
var router = express.Router();
var path = require('path');

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

router.get('/user',(req,res,next)=>{
	next();
},(req,res,next)=>{
	var file = path.resolve('data dumps','campaign_data.json');

	fs.readFile('/home/abhinav/Hackathons/angehack16-jaipur/data dumps/campaign_data.json','utf-8',(err,data) =>  {
		if(err)
			res.send(err);
		else
			{
					req['campaign_data'] = data;
					next();
			}	
	});
},(req,res,next) => {
	fs.readFile('/home/abhinav/Hackathons/angehack16-jaipur/data dumps/user_data.json','utf-8',(err,data) => {
		if(err)
			res.send(err);
		else
		{
			let campaign_data = JSON.parse(req.campaign_data);
			let user_data = JSON.parse(data);
			let userId = req.query.id;

			let campaigns = user_data[userId]["my_campaigns"];
			let plot_data = [];
			campaigns.forEach((campaign) => {
				campaign_data.forEach((cd) => {
					if(cd["_id"] == campaign["c_id"]){
						plot_data.push(cd);
					}
				});
			});

			let x = plot_data.map(datum => datum.name);
			let y = plot_data.map(datum => datum.donation_received);

			var graphOptions = {filename: "basic-bar", fileopt:"overwrite"};
			/*plotly.plot([{x,y,type:"bar"}],graphOptions,(err,msg) => {
				if(err)
					res.send(err);
				else
					res.send(msg);
			});*/

			plotly.getImage({'data':[{x,y,type:"bar"}]},{format:'png',width:1000,height:500},(err,imgStream) => {
				if(err)
					res.send(err);
				else
					imgStream.pipe(fs.createWriteStream('img.png'));
					res.sendFile(path.resolve('img.png'));
			});
		}
			
	});
});

module.exports = router;

