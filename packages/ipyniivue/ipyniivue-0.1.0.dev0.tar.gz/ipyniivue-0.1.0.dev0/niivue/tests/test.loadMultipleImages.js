const { snapshot, httpServerAddress, seconds } = require("./helpers")
beforeEach(async () => {
  await page.goto(httpServerAddress, {timeout:10000})
  await page.setViewport({width: 1440, height: 900, deviceScaleFactor: 1});
})
test('overlay', async () => {
  let nvols = await page.evaluate(async () => {
    nv = new niivue.Niivue()
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
      {
        url: "../images/hippo.nii.gz",//"./RAS.nii.gz", "./spm152.nii.gz",
        volume: { hdr: null, img: null },
        name: "hippo.nii.gz",
        colorMap: "winter",
        opacity: 1,
        visible: true,
      },
    ]
    await nv.loadVolumes(volumeList)
    return nv.volumes.length
  })

  expect(nvols).toBe(2)
  await snapshot()
})
