# CHNRoutes_For_WARP
A python script which can generate TWO scripts for CLOUDFLARE WARP.

纯粹就是为了生成两个文件，防止在给自己的VPS套CLOUDFLARE WARP时路由了中国大陆的IP地址。
参考了（其实是抄了）[chnroutes](https://github.com/fivesheep/chnroutes) 项目，为了方便自己，所以Push到Github上来。

## 使用
在对应的wg conf的Interface下写入：
PostUp = bash /path/to/your/chnrouteup
PostDown = bash /path/to/your/chnroutedown

最后更新：2021年6月6日

