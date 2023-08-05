const { snapshot, httpServerAddress, seconds } = require("./helpers")
beforeEach(async () => {
  await page.goto(httpServerAddress, {timeout:0})
  await page.setViewport({width: 1440, height: 900, deviceScaleFactor: 1});
})
test('sets slice type sagittal', async () => {
  await page.evaluate(async () => {
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
    nv.setSliceType(nv.sliceTypeSagittal)
    return
  })

  // take a snapshot for comparison
  await snapshot()

})