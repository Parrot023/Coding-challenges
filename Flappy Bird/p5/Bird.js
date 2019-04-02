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
