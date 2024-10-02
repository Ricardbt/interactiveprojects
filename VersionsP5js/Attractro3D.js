let a, b, c, d, z, xn, yn;
let x, y;

function setup() {
  a = 0.970;
  b = -1.899;
  c = 1.381;
  d = -1.506;
  z = 20;
  xn = 500;
  yn = 300;
  
  createCanvas(1080, 1920, WEBGL);
  background(255);
  noFill();
}

function draw() {
  background(255); // Clear the background in each frame
  translate(0, 0, 0); // Center the canvas for 3D rotation
  
  // Calculate x, y coordinates based on sine and cosine functions
  x = (sin(a * yn) + c * cos(a * xn)) * 120;
  y = (sin(b * xn) + d * cos(b * yn)) * 120;
  
  z += 0.5; // Increment z for rotation
  
  // Draw the ellipse
  stroke(x, y, z);
  ellipse(x, y, 2, 2);
  
  // Rotate the shape around the Y axis
  rotateY(radians(z));
  
  beginShape();
  for (let t = 0; t <= 120; t += 5) {
    vertex(x + t, y + t);
    for (let s = 0; s <= 120; s += 4) {
      vertex(s, t);
    }  
  }
  endShape();
  
  // Update xn and yn for the next frame
  xn += 0.015;
  yn += 0.015;
}
