<h2>Use</h2>
A multi-purpose tracking system with modular design. Users can add customized modules for different purposes. For example, tracking gold price, stock price, online deals and etc. Users can also configure the frequency of the sms notifications.


![Optional Text](../master/example.jpg)



<h2>Prerequisite</h2>
<ol>
  <li>AWS account <ul>

  </ul></li>
  <li>ECR service <ul>

  </ul></li>
  <li>ECS service <ul>
 
  </ul></li></li>
  <li>Twilio account <ul>

  </ul></li>
</ol>

<h2>Configuration</h2>
config.ini

<ol>
  <li>Stock price <ul>
      <li>Ticker name</li>
      <li>Price</li>
      <li>Notification time</li>
  </ul></li>
  <li>Gold <ul>
      <li>Price</li>
      <li>Notification time</li>
  </ul></li>
</ol>


<h2>Deployment</h2>
deploy.sh

<ol>
  <li>Build the docker image <ul>

  </ul></li>
  <li>Push the docker image to AWS ECR <ul>

  </ul></li>
  <li>Restart the task in the ECS service <ul>
  
  </ul></li>
</ol>

