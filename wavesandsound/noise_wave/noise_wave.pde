/**
 * Noise Wave
 * by Daniel Shiffman.  
 * 
 * Using Perlin Noise to generate a wave-like pattern. 
 */

float yoff = 0.0;        // 2nd dimension of perlin noise
 NoiseWave noiseWave;
void setup() {
  size(1440, 860);
    noiseWave = new NoiseWave();
}

void draw() {
  background(85, 25, 94);
   float xoff = 0;  
   float t = map(noise(0, mouseX), 0, 5, 0,255);
   stroke(t, 80 , mouseY/4);
  strokeWeight(6);
  
   
     fill(95, 15, 64);
  // We are going to draw a polygon out of the wave points
  beginShape();  
     // Iterate over horizontal pixels
  for (float x = 0; x <= width; x += 10) {
    // Calculate a y value according to noise, map to 
    float y = map(noise(xoff, yoff), 0, 2, 200,400); // Option #1: 2D Noise
    // float y = map(noise(xoff), 0, 1, 200,300);    // Option #2: 1D Noise
    
    // Set the vertex
    vertex(x, y); 
    // Increment x dimension for noise
    xoff += 0.27;
  }
  // increment y dimension for noise
  yoff += 0.02;
  vertex(width, height);
  vertex(0, height);
  endShape(CLOSE);
  
     stroke(t, 180 , mouseY/2);
  strokeWeight(4);
   fill(251, 139, 36);
     noiseWave.drawWave(2, 150, 900); 
    fill(227, 100, 20);
     noiseWave.drawWave(4, 350, 700); 
     
       fill(154, 3, 30);
     noiseWave.drawWave(6, 550, 400); 
        stroke(t, 40 , mouseY/6);
  strokeWeight(3);
         fill(154, 53, 30);
     noiseWave.drawWave(2, 650, 560); 
     
      fill(124, 3, 20);
      
      noiseWave.drawWave(8, 750, 200); 

  // increment y dimension for noise
  yoff += 0.02;
  vertex(width, height);
  vertex(0, height);
  endShape(CLOSE);

}
