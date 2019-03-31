
//objects
var bird;
var walls = [];
var numOfWalls;

function setup() {

  //height and width
  let height = 400;
  let width = 400;
  //it is best to keep the nunber of walls below three due to a little bug
  //you can try and do it and see if you can find it :-)
  numOfWalls = 2;


  //creates canvas
  createCanvas(width, height);
  //sets background to black
  background(0);

  bird = new player()
  for (let i = 0; i < numOfWalls; i++) {
    walls[i] = new wall(width + i * 200);
  }

  // put setup code here
}


function draw() {
  background(0);
  // console.log(width)
  bird.show();
  bird.update();

  for (let i = 0; i < numOfWalls; i++) {
    walls[i].show()
    walls[i].update()
    walls[i].encounter(bird)
  }
}

//keypressed is a p5.js function
//it is called when ever a key is pressed
function keyPressed() {

  //keycode 32 is the ASCII code for Space Bar
  if (keyCode === 32) {
    bird.jump()
  }
}


function player() {

  this.x = width / 2;
  this.y = height / 2;
  this.w = 10;
  this.acc = 0.1;
  this.vel = 0;

  this.show = function() {
    fill(255);
    circle(this.x, this.y, this.w)
  }

  this.update = function() {
    this.vel += this.acc;
    this.y += this.vel;
  }

  this.jump = function() {
    this.vel -= 5;
  }
}




function wall(x) {

  this.w = 10;
  this.h = random(50, 350);
  this.y = height - this.h;
  this.x = x;
  this.hit = false;
  this.gab = 60;

  this.show = function() {

    //true if hit is true
    if (this.hit) {
      fill(255,0,0);

    //true if hit is not true
    } if (!(this.hit)) {
      fill(255);
    }

    //draws bottom and top part of wall
    rect(this.x, this.y, this.w, this.h); //bottom
    rect(this.x, 0, this.w, height - this.h - this.gab); //top
    console.log(this.collapse)
  } //-------- end of show()

  this.update = function() {
    this.x -= 1;

    //true if the walls x is of the screen
    if (this.x < 0) {

      this.x = width;
      this.h = random(50, 350);
      this.gab = random(40,60);
      this.y = height - this.h;

    }
  } //------ end of update()

  this.encounter = function(bird) {

    //true if the bird hits the bottom part of the wall
    if (bird.x > this.x && bird.x < this.x + this.w) {
      if (bird.y > this.y && bird.y < this.y + height) {
        this.hit = true;
      }
    } else {
      this.hit = false;
    }

    //true if the bird hits the top part of the wall
    if (bird.x > this.x && bird.x < this.x + this.w) {
        if (bird.y > 0 && bird.y < this.y - this.gab) {
          this.hit = true;
        }
    } else {
      this.hit = false;
    }
  } //------------ end of encounter()
} //-------------- end of wall object
