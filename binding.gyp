{
  "targets": [
    {
      "target_name": "libtorrent",
      "product_name": "libtorrent",
      "sources": [
      	"src/module.cpp",

        "src/add_torrent_params.cpp",
        "src/bencode.cpp",
        "src/create_torrent.cpp",
        "src/entry.cpp",
        "src/file_storage.cpp",
        "src/fingerprint.cpp",
        "src/session.cpp",
        "src/storage.cpp",
        "src/torrent_handle.cpp",
        "src/torrent_info.cpp",
        "src/torrent_status.cpp"
      ],
      "cflags_cc": [
        "-fPIC",
        "`pkg-config --cflags libtorrent-rasterbar`"
      ],
      "cflags_cc!": [
        "-fno-exceptions"
      ],
      "ldflags": [],
      "libraries": [
        "`pkg-config --libs libtorrent-rasterbar`"
      ],
      "conditions": [
        ["OS=='linux'", {  
        }]
      ]
    }
  ]
}
