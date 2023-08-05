const { snapshot, httpServerAddress, seconds } = require("./helpers")
beforeEach(async () => {
  await page.goto(httpServerAddress, {timeout:0})
  await page.setViewport({width: 1440, height: 900, deviceScaleFactor: 1});
})
test('vox2frac', async () => {
  let frac = await page.evaluate(async () => {
    let opts = {
      textHeight: 0.05, // larger text
      crosshairColor: [0, 0, 1, 1] // green
    }
    let nv = new niivue.Niivue(opts = opts)
    await nv.attachTo('gl')

    // load one volume object in an array
    var volumeList = [
      {
        url: "../images/mni152.nii.gz",//"./RAS.nii.gz", "./spm152.nii.gz",
        volume: { hdr: null, img: null },
        name: "mni152.nii.gz",
        colorMap: "gray",
        opacity: 1,
        visible: true,
      },
    ]
    
    await nv.loadVolumes(volumeList)
    let vox = [103, 128, 129]
    let frac = nv.vox2frac(vox)
    
    return frac
  })
  expected = [0.5000415009576917, 0.5017796754837036, 0.6023715706758721]
  for (let i=0; i<frac.length; i++){
    expect(frac[i]).toBeCloseTo(expected[i])
  }
})