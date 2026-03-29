// parser.js
import { parse } from 'csv-parse';
import { Readable } from 'stream';
import { v4 as uuidv4 } from 'uuid';

const parseFile = (fileBuffer) => {
  const fileStream = new Readable();
  fileStream.push(fileBuffer);
  fileStream.push(null);

  return new Promise((resolve, reject) => {
    const parser = parse({
      from: fileStream,
      delimiter: ',',
      columns: true,
      skip_empty_lines: true,
    });

    const data = [];

    parser.on('readable', () => {
      let record;
      while ((record = parser.read())!== null) {
        data.push(record);
      }
    });

    parser.on('end', () => {
      resolve(data);
    });

    parser.on('error', (err) => {
      reject(err);
    });
  });
};

const generateId = () => uuidv4();

export { parseFile, generateId };