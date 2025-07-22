const express = require('express');
const multer = require('multer');
const { spawn } = require('child_process');
const path = require('path');

const router = express.Router();
const upload = multer({ dest: 'uploads/' });

router.post('/verify', upload.fields([{ name: 'aadhaar' }, { name: 'selfie' }]), async (req, res) => {
  const aadhaarPath = req.files['aadhaar'][0].path;
  const selfiePath = req.files['selfie'][0].path;

  const python = spawn('python3', ['face_match.py', aadhaarPath, selfiePath], {
    cwd: path.join(__dirname, '..')
  });

  let output = '';
  python.stdout.on('data', (data) => output += data.toString());
  python.stderr.on('data', (data) => console.error("Python error:", data.toString()));

  python.on('close', () => {
    output = output.trim();
    if (output.startsWith("ERROR")) {
      return res.status(400).json({ error: output });
    } else if (output.startsWith("PASS")) {
      const confidence = 100 - parseFloat(output.split(":")[1]) * 100;
      return res.json({ match: true, confidence: confidence.toFixed(2) });
    } else {
      const confidence = 100 - parseFloat(output.split(":")[1]) * 100;
      return res.json({ match: false, confidence: confidence.toFixed(2) });
    }
  });
});

module.exports = router;
