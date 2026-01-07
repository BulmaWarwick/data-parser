const fs = require('fs');
const csv = require('csv-parser');
const { console } = require('console');

class DataParser {
  constructor(file_path) {
    this.file_path = file_path;
    this.data = [];
  }

  async parseFile() {
    try {
      return new Promise((resolve, reject) => {
        fs.createReadStream(this.file_path)
          .pipe(csv())
          .on('data', (row) => {
            this.data.push(row);
          })
          .on('end', () => {
            resolve(this.data);
          })
          .on('error', (error) => {
            reject(error);
          });
      });
    } catch (error) {
      console.error(`Error parsing file: ${error}`);
      throw error;
    }
  }

  async saveDataToFile(file_path) {
    try {
      const csv_data = this.data.map((row) => Object.values(row).join(',')).join('\n');
      await fs.promises.writeFile(file_path, csv_data);
    } catch (error) {
      console.error(`Error saving data to file: ${error}`);
      throw error;
    }
  }
}

module.exports = DataParser;