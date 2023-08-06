from simauth import simauth

accounts = {'gAAAAABj3m4DX157Xvi4T7E5d3D3evOm0SN3wOck2mMq01dDhDCYJbWVYqe_FinetQExZrxL4xzjK074wBrv14a00QV3xUifpg==': 'gAAAAABj3m4EZE74wInGUJSs7ft2O51kK-z6uzN7vCw_CwURk-Xu70vnsomJBFVbFjvc32B1LNTDYU_UCiqc4HbJV69Aew3eOIOn5ljQxBoSfULXLgQ5I30tK_xpXPd98qbH1Zv77e-Z', 'gAAAAABj3m4E_HiJgjgYC1FyxazPB0M4LkYqgugCtT8fw_gGLxKxc5B9_VIkve7RNCdoawPtwsHogK-1dhzh0xnIxhyZDWr0Jw==': 'gAAAAABj3m4EaDvMyZuOOtz3XUjtwEbEeFXWBtOJfaa-DLrB55vK_kT71cGIHrmRwYtbWqJgpoWm_ROKrCKo6U4TPtQ2ertiwkn_N8w-Fxb8N_Xu6Ba6NxXTGNl5G6JOQZYvHISvWqxT'}
paths = ['~/.config/hema_fernet_key', '/data/hema_fernet_key', './local/fernet.key']

auth = simauth(accounts, paths)
