public class NoiseWave {

  float xoff, yoff;

  void drawWave(float noiseValue, float xValue, float yValue) {
    beginShape();
    xoff = 0; // Option #1: 2D Noise

    // Iterate over horizontal pixels
    for (float x = 0; x <= width; x += 8) {
      // Calculate a y value according to noise, map to 
      float y = map(noise(xoff, yoff), 0, noiseValue, xValue, yValue); // Use variables
      // float y = map(noise(xoff), 0, 1, 200, 300);    // Option #2: 1D Noise

      // Set the vertex
      vertex(x, y); 
      // Increment x dimension for noise
      xoff += 0.3;
    }
    // increment y dimension for noise
    yoff += 0.02;
    vertex(width, height);
    vertex(0, height);
    endShape(CLOSE);
  }
}
