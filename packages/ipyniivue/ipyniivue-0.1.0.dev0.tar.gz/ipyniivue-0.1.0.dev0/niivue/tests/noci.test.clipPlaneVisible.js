const { snapshot, httpServerAddress, seconds } = require("./helpers")
beforeEach(async () => {
  await page.goto(httpServerAddress, {timeout:0})
  await page.setViewport({width: 1440, height: 900, deviceScaleFactor: 1});
})
test('clip plane is rendered when it is set to visible', async () => {
  await page.evaluate(async () => {
    let opts = {
      textHeight: 0.05, // larger text
      crosshairColor: [0, 0, 1, 1] // green
    }
    let nv = new niivue.Niivue(opts = opts)
    
    await nv.attachTo('gl')
    nv.sliceType = nv.sliceTypeRender;
    nv.clipPlaneObject3D.isVisible = true;

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
  })
  // take a snapshot for comparison
  await snapshot()

})