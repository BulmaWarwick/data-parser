const fs = require('fs');
const path = require('path');

class Parser {
  constructor(config) {
    this.config = config;
    this.data = {};
  }

  parse(filePath) {
    const fileContent = fs.readFileSync(filePath, 'utf8');
    const lines = fileContent.split('\n');
    lines.forEach(line => {
      const [key, value] = line.split(':');
      this.data[key.trim()] = value.trim();
    });
  }

  writeOutput(outputFilePath) {
    const outputContent = Object.entries(this.data).map(([key, value]) => `${key}: ${value}`).join('\n');
    fs.writeFileSync(outputFilePath, outputContent);
  }

  validateConfig() {
    if (!this.config.filePaths) {
      throw new Error('File paths are required in the config.');
    }
    if (!this.config.outputPath) {
      throw new Error('Output path is required in the config.');
    }
  }
}

module.exports = Parser;