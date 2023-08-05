const { snapshot, httpServerAddress, seconds } = require("./helpers")
beforeEach(async () => {
  await page.goto(httpServerAddress, {timeout:0})
  await page.setViewport({width: 1440, height: 900, deviceScaleFactor: 1});
})
test('wasm process image replace', async () => {
  await page.evaluate(async () => {
    let nv = new niivue.Niivue()
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
    let niimathCmd = "-dog 1 1.6"
    let addAsOverlay = false
    // use niimath wasm to process image  (dog command shows edges)
    nv.processImage(0, niimathCmd, addAsOverlay)
  })
  // snapshot should be edges
  await snapshot()
})