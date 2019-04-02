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
