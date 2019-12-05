

let P1_bat;
let P2_bat;
let change_y = 10;
let bat_height = 100;
let bat_width = 10;
let ball;
let ball_d = 50;
let ball_change_x = 5;
let ball_change_y = 2;

function setup() {
  //canvas
  createCanvas(500,500);
  frameRate(60)

  //Initiate players and ball
  P1_bat = [0 + 20, height / 2];
  P2_bat = [width - 20, height / 2];
  ball = [width / 2, height / 2];
  

}

function draw() {

  if (frameCount % 300 == 0) {
    ball_change_x *= 1.1;
    ball_change_y *= 1.1;
  }

  background(100);

  //Draw player 1 and 2
  rectMode(CENTER);
  rect(P1_bat[0], P1_bat[1], bat_width, bat_height)
  rect(P2_bat[0], P2_bat[1], bat_width, bat_height)

  //Draw ball
  ellipse(ball[0], ball[1], ball_d)
  //Update ball location
  ball[0] += ball_change_x;
  ball[1] += ball_change_y;

  //Calculate ball hitbox
  ball_bottom = ball[1] + ball_d / 2;
  ball_top = ball[1] - ball_d / 2;
  ball_right = ball[0] + ball_d / 2;
  ball_left = ball[0] - ball_d / 2;

  //If hit player 1
  if (ball_top < P1_bat[1] + bat_height / 2 && ball_bottom > P1_bat[1] - bat_height / 2) {
    if (ball_left < P1_bat[0] + bat_width) {
      ball_change_x *= -1;
    }
  }
  //If hit player 2
  if (ball_top < P2_bat[1] + bat_height / 2 && ball_bottom > P2_bat[1] - bat_height / 2) {
    if (ball_right > P2_bat[0] - bat_width / 2   && ball_left) {
      ball_change_x *= -1;
    }
  }

  //If hit the top
  if (ball_top <  0 || ball_bottom > height) {
    ball_change_y = ball_change_y * -1;
  }

  if (ball_left < 0 || ball_right > width) {
    ball = [width/2, height/2]
  }


}


function keyPressed() {

  //Moving player 1 and 2
  if (keyCode == UP_ARROW) {
    P2_bat[1] -= 30; 
  } else if (keyCode == DOWN_ARROW) {
    P2_bat[1] += 30;
  } else if (keyCode == 87) {
    P1_bat[1] -= 30; 
  } else if (keyCode == 83) {
    P1_bat[1] += 30;
  }
}